from flask import Flask, render_template, request, jsonify, send_from_directory,redirect,url_for,session
import requests
import base64
import os
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

app = Flask(__name__)

PAYPAL_CLIENT_ID = "AZ4jdHpd4seEuaMFQL7ItNiVArMl06W3G30Y1aErCbKM0N0cWUhRMMxkyysnMt9p6snkg9k-8MFmF311"
PAYPAL_CLIENT_SECRET = "EKIsp9-6e2RAK6Rs_ilhluyHuSbprASf6HYQQs5wZ5CuN3avKulrAqKK8FGojYPbfv1FVzm-_y9Hzndy"
BASE_URL = "https://api-m.sandbox.paypal.com"


app.secret_key=''

app.secret_key='sec'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '22Million$'
app.config['MYSQL_DB']='usertesting'

mysql=MySQLdb.connect('localhost','root','22Million$','usertesting')
cursor = mysql.cursor()
#Display Webpage

@app.route('/admin', methods=['GET','POST'])
def admin():
    session['loggedin']=False
    errorMsg=''
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        username=request.form['username']
        password=request.form['password']

        cursor.execute('SELECT * FROM usertable WHERE users =\''+username+'\' AND passwords =\''+password+'\'')
        account=cursor.fetchone()

        if account:
            session['loggedin']=True
            
        else: errorMsg='incorrect login'
    return render_template('admin.html', msg=errorMsg)

@app.route("/")
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

@app.route('/editClass')
def editClass():
  with open("client\changeClasses.py") as file:
    try:
        exec(file.read())
    except Exception as e:
        return f'Error executing script: {str(e)}'

@app.route('/editEvents')
def  editEvents():
  with open("client\changeEvents.py") as file:
    try:
        exec(file.read())
    except Exception as e:
        return f'Error executing script: {str(e)}'
    
@app.route('/editMerch')
def  editMerch():
  with open("client\changeMerch.py") as file:
    try:
        exec(file.read())
    except Exception as e:
        return f'Error executing script: {str(e)}'

@app.route('/api/orders', methods=['POST'])
def create_create_order():
    try:
        data = request.json
        cart = data.get('cart', [])
        # Ensure total is calculated as a string formatted to two decimal places
        total = "{:.2f}".format(sum(item['amount'] * item['quantity'] for item in cart))

        access_token = generate_access_token()
        url = f"{BASE_URL}/v2/checkout/orders"
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [{
                "amount": {
                    "currency_code": "USD",
                    "value": total  # Use the dynamically calculated total here
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
    app.run(port=5000)

if __name__ == '__main__':
  app.run(debug=True)