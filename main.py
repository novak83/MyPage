from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hire", methods=["GET", "POST"])
def hire():
    if request.method == "GET":
        return render_template("hire.html")
    elif request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print(name)
        print(email)
        print(message)

        return render_template("success.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("portfolio/boogle.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("portfolio/fakebook.html")

@app.route("/portfolio/hairsalon")
def hairsalon():
    return render_template("portfolio/hairsalon.html")

@app.route("/my_other_hobby")
def hobby():
    return render_template("my_other_hobby.html")

if __name__ =='__main__':
    app.run(use_reloader=True, debug=True)