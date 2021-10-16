from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'fcb4d56dc328bbb269db411972547c41'

posts = [
    {
        'author' : 'Siddhi',
        'title' : 'Neural Style Transfer',
        'content' : '''Implementation of Neural Style Transfer inspired from code available at official tensorflow website. Implemented single style transfer.''',
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


@app.route("/contact", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Craeted for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)




if __name__=='__main__':
    app.run()
