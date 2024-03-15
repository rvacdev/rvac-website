from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user

app = Flask(__name__)


'''
#CHANGE LOCATION OF DATBASE TO CONNECT TO THE ACCTUAL DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

#EDIT THE SECRET KEY
app.config['SECRET_KEY']='ENTER SECRET KEY'

db=SQLAlchemy()

manager=LoginManager()
manager.init_app(app)

class Users(UserMixin,db.Model):
  #CHANGE THESE VALUES TO MATCH OUR DATABASE
  id=db.column(db.String(250), unique=True,
                         nullable=False)
  password = db.Column(db.String(250),
                         nullable=False)

db.init_app(app)

with app.app_context():
    db.create_all()

@manager.user_loader
def loader_user(userID):
   return Users.query.get(userID)
'''


#Display Webpage

@app.route('/admin', methods=["GET",'POST'])
def admin():
  if request.method=='POST':
     '''user=Users.query.filter_by(username=request.form.get("username")).first()
     if user.password==request.form.get('password'):
        login_user(user)
        return render_template('admin.html')'''
  return render_template('admin.html')

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

if __name__ == '__main__':
  app.run(debug=True)