from flask import Flask , render_template,request
from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb://localhost:27017/")
db = client["BusBro"]
users = db["users"]
feedbacks = db["feebacks"]

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/result",methods=["POST"])
def submit():
    fname = request.form.get('username')
    password = request.form.get('password')
    user = {
        "FullName" : fname,
        "Password" : password
    }
    users.insert_one(user)
    return render_template('result.html',fname=fname,passw=password)

@app.route("/adminpage")
def admin():
    usersdata = list(users.find())
    return render_template("adminpage.html",usersdata=usersdata)


@app.route("/feedback")
def feed():
    return render_template("feedback.html")


@app.route("/feedbacksubmit", methods=["POST"])
def submitfeed():
    fname = request.form.get("fname")
    message = request.form.get("mess")
    date = datetime.now()
    feed = {"FullName" : fname , "message" : message , "date" : date}
    feedbacks.insert_one(feed)
    return render_template("feedbacksubmit.html",fname=fname,message=message,date=date)

@app.route("/adminfeedbacks")
def adminfeed():
    feedbacksdata = list(feedbacks.find())
    return render_template("adminfeedbacks.html", feedbacksdata=feedbacksdata)

if (__name__=="__main__"):
    app.run(debug=True)