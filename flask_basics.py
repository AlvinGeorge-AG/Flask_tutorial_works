from flask import Flask,render_template,url_for

postdata = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html', posts=postdata, title='Its a home page')


@app.route('/about')
def about():
    return render_template('about.html',title="Its an about page")

if __name__ =='__main__':
    app.run(debug=True)