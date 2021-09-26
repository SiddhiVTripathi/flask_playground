from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from time import sleep
from datetime import datetime
from flask_sqlalchemy import fSQLAlchemy
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fcb4d56dc328bbb269db411972547c41'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default ='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author',lazy=True)

    def __repr__(self):
        return f"'User('{self.username}','{self.email}','{seld.image_file}')"


class Post(db.Model):
    id          = db.Column(db.Integer,primary_key=True)
    title       = db.Column(db.String(100),nullable = False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content     = db.Column(db.Text, nullable=False)
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted})"
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
    return render_template('home.html', posts=posts, title="Home")


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Craeted for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("Welcome back")
            sleep(5)
            return redirect(url_for('home'))
        else:
            flash("Please check your username ans password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__=='__main__':
    app.run(debug=True)
