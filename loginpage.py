import session,url_for,redirect
@app.route("/login",methods=['GET','POST'])
def login():
    r = " "
    mgs = " "
    if(request.method == "POST"):
    username = request.form["username"]
    password = request.form["password"]
    conn = dqlite3.connect(food transactions.db)
    c = conn.cursor()
    c.execute("SELECT * FROM person WHERE username = '"+username+"'and password ='"+password"')
    r = c.fetchall()
    for i in r:
    if(username == i[0] and password == i[1]):
        session["loggedin"] = True 
        session["username"] = username
        return redirect(url_for("about"))
    else:
        mgs = "Please Enter Valid username and password"
        return render_template("login.html",mgs =mgs)