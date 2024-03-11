from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def admin():
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

if __name__ == '__main__':
  app.run(debug=True)