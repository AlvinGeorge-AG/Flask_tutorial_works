from flask import Flask , render_template , request

app = Flask(__name__)
busdata=['ksrtc', 'ksrtc-swift','private-bus','Super-Duelux']
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/about')
def  about():
    return render_template('about.html')

@app.route('/user')
def user():
    return render_template('userpag.html',user="Alvin George")

@app.route("/buses")
def buses():
    return render_template("buses.html",data = busdata)

@app.route("/profile")
def pro():
    return render_template("profile.html",name="Joyal C Kurian",age =19,hobby="Sleeping")


@app.route("/signup")
def signup():
    return  render_template("signup.html") 


@app.route("/submit",methods=["POST"])
def submit():
    fname = request.form.get("fname")
    age = request.form.get("age")
    password = request.form.get("passw")
    email = request.form.get("email")
    return render_template("submit.html",fname=fname,age=age,passw=password,email=email)

if (__name__=="__main__"):
    app.run(debug=True)
