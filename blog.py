from flask import Flask, render_template, url_for, 
from forms import RegistraForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY''] = 'e0f3e1e5f2b7d4ee38c450248adc0bd1'

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

@app.route("/register")
def register():
  from = RegistrationForm()
  return render_template('register.html', title='Register', form =form)


@app.route("/login")
def login():
  from = LoginForm()
  return render_template('login.html', title='login', form =form)

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port=5000)
