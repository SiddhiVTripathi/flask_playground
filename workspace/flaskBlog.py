from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Siddhi',
        'title' : 'First Blog',
        'content' : 'First Post content',
        'date_posted' : 'April 14, 2020'
    },

    {
        'author' : 'John Doe',
        'title' : 'Second Blog',
        'content' : 'Second Post content',
        'date_posted' : 'April 15, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


if __name__=='__main__':
    app.run(debug=True)
