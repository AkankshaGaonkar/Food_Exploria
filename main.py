import sqlite3
from flask import Flask , render_template , redirect , url_for , request , session

app = Flask(__name__)

cake_names = ["Black Forest", "Choco Lava", "Red Velvet", "Ferrero Rocher"]
prices = [300, 450, 400, 550]

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", data = cake_names, prices = prices)
    # return render_template("index.html")

if __name__ == '__main__':
    secret_key = "chandaGompi"
    app.run(debug = True)

