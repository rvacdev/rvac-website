from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
import base64
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user

app = Flask(__name__)

PAYPAL_CLIENT_ID = "AZ4jdHpd4seEuaMFQL7ItNiVArMl06W3G30Y1aErCbKM0N0cWUhRMMxkyysnMt9p6snkg9k-8MFmF311"
PAYPAL_CLIENT_SECRET = "EKIsp9-6e2RAK6Rs_ilhluyHuSbprASf6HYQQs5wZ5CuN3avKulrAqKK8FGojYPbfv1FVzm-_y9Hzndy"
BASE_URL = "https://api-m.sandbox.paypal.com"


#CHANGE LOCATION OF DATBASE TO CONNECT TO THE ACCTUAL DATABASE
'''app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

#EDIT THE SECRET KEY
app.config['SECRET_KEY']='ENTER SECRET KEY'

db=SQLAlchemy()

manager=LoginManager()
manager.init_app(app)

class Users(UserMixin,db.Model):
  #CHANGE THESE VALUES TO MATCH OUR DATABASE
  id=db.column(db.String(250), unique=True,nullable=False)
  password = db.Column(db.String(250),nullable=False)

db.init_app(app)

with app.app_context():
    db.create_all()

@manager.user_loader
def loader_user(userID):
   return Users.query.get(userID)'''



#Display Webpage

@app.route('/', methods=["GET",'POST'])
def admin():
  '''if request.method=='POST':
     user=Users.query.filter_by(username=request.form.get("username")).first()
     if user.password==request.form.get('password'):
        login_user(user)
        return render_template('admin.html')'''
  return render_template('admin.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/calendar")
def calendar():
    return render_template('calendar.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/checkout")
def checkout():
    return render_template('checkout.html')

@app.route("/class")
def classpage():
    return render_template('class.html')

@app.route("/memberdon")
def memberdon():
    return render_template('memberdon.html')

@app.route('/editClass/')
def editClass():
  with open("changeClasses.py") as file:
    exec(file.read())

@app.route('/editEvents/')
def  editEvents():
  with open("changeEvents.py") as file:
    exec(file.read())

@app.route('/editMerch/')
def  editMerch():
  with open("changeMerch.py") as file:
    exec(file.read())

@app.route('/api/orders', methods=['POST'])
def create_order():
    try:
        cart = request.json.get('cart')
        access_token = generate_access_token()
        url = f"{BASE_URL}/v2/checkout/orders"
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    "currency_code": "USD",
                    "value": "100.00"
                }
            }]
        }

        response = requests.post(url, json=payload, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        })

        return handle_response(response)

    except Exception as e:
        print("Failed to create order:", e)
        return jsonify(error="Failed to create order."), 500

@app.route('/api/orders/<orderID>/capture', methods=['POST'])
def capture_order(orderID):
    try:
        access_token = generate_access_token()
        url = f"{BASE_URL}/v2/checkout/orders/{orderID}/capture"

        response = requests.post(url, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        })

        return handle_response(response)

    except Exception as e:
        print("Failed to capture order:", e)
        return jsonify(error="Failed to capture order."), 500

def generate_access_token():
    try:
        if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
            raise Exception("MISSING_API_CREDENTIALS")

        auth = base64.b64encode(f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}".encode()).decode('utf-8')
        response = requests.post(f"{BASE_URL}/v1/oauth2/token", data="grant_type=client_credentials", headers={
            "Authorization": f"Basic {auth}"
        })

        data = response.json()
        return data['access_token']

    except Exception as e:
        print("Failed to generate Access Token:", e)

def handle_response(response):
    try:
        json_response = response.json()
        return jsonify(json_response), response.status_code
    except Exception as e:
        error_message = response.text
        return jsonify(error_message=error_message), response.status_code

@app.route('/')
def serve_index():
    return send_from_directory('client', 'checkout.html')

if __name__ == "__main__":
    app.run(port=PORT)

if __name__ == '__main__':
  app.run(debug=True)