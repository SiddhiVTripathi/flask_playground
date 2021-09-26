from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fcb4d56dc328bbb269db411972547c41'

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
            return redirect(url_for('home'))
        else:
            flash("Please check your username ans password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__=='__main__':
    app.run(debug=True)
