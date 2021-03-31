import sqlite3
from flask import Flask , render_template , redirect , url_for , request , session

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("webpagehome.html")

if __name__ == '__main__':
    app.run(debug = True)