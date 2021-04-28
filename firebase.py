import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyADuAAM5WYt_m6N4iU0gIA3ID4rggmqmBw",
    'authDomain': "food-exploria.firebaseapp.com",
    'projectId': "food-exploria",
    'storageBucket': "food-exploria.appspot.com",
    'messagingSenderId': "303710504686",
    'appId': "1:303710504686:web:f35d2d044509cb90b8d5ff",
    'measurementId': "G-J0WHDB51SB"
}
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

#login fuction

def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
       
    except:
        print("Invalid email or password")
    return

#Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

#Main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()
