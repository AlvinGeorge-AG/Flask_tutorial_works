from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    message = {"mess": "HELLO FROM ALVIN USING FLASK BACKEND !"}
    return message
if(__name__=="__main__"):
    app.run(debug=True)