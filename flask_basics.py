from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html', title='Its a home page')


@app.route('/about')
def about():
    return render_template('about.html',title="Its an about page")

if __name__ =='__main__':
    app.run(debug=True)