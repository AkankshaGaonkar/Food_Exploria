import sqlite3
from flask import Flask , render_template , redirect , url_for , request , session

app = Flask(__name__)

cake_names = ["Black Forest", "Choco Lava", "Red Velvet", "Ferrero Rocher"]
prices = [300, 450, 400, 550]

@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':      
        id = request.form['UID']
        password = request.form['PW']
        #we have to check whether user entered credentials if it matches then he is redirected home page otherwise not
        return redirect("/home")
    else:
        return render_template("login.html", invalid = True)

@app.route('/adminlogin', methods = ['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':
        name = request.form["username"]
        pw = request.form['pw']
        print(name, pw)
        if(name == 'admin' and pw == 'admin'):
            return redirect('/home')
        else:
            return render_template('admin_login.html', invalid = False)
    else:
        return render_template('admin_login.html', invalid = True)

@app.route("/home")
def index():
    return render_template("home.html", data = cake_names, prices = prices)
    # return render_template("index.html")

@app.route("/cart", methods = ['GET', 'POST'])
def cart():
    if request.method == 'POST':
        name = request.form["cakeName"]
        qty = request.form["qty"]
    return name+" "+qty
    
if __name__ == '__main__':
    secret_key = "chandaGompi,BM"
    app.run(debug = True)

