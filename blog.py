from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = "e0f3e1e5f2b7d4ee38c450248adc0bd1"

posts = [
  {
    'author':'abishek',
    'title': 'Bolg post 1',
    'content': 'First posrt',
    'date_posted': 'jan 20, 2023'
  },
  {
    'author':'abi',
    'title': 'Blog Post 2',
    'content': 'Second posrt',
    'date_posted': 'jan 25, 2023'
  }
]


@app.route("/home")
def home():
  return render_template("home.html", posts=posts)


@app.route("/about")
def about():
  return render_template("about.html", title='About')

@app.route("/register", methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form = form)


@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == '123':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='login', form = form)

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port=5000)
