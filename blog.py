from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port=5000)
