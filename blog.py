from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = "e0f3e1e5f2b7d4ee38c450248adc0bd1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Cloumn(db.String(20), unique=True, nullable=False)
  email = db.Cloumn(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20),nullable=False, default='default.png')
  password = db.Column(db.String(60), nullable=False)
  posts = db.relationship('post', backref='author', lazy = True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
  


  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"


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
