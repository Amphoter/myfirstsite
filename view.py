from app import app, db
from flask import request, render_template, redirect
from models import UserInfo
from calc import calculator


@app.route('/')
@app.route('/home')
def home():
    return render_template("homepage.html")


@app.route('/users', methods=['GET'])
def users():
    try:
        users = UserInfo.query.all()

        return render_template("users.html", users=users)
    except:
        return render_template("Error.html",Error="No users")


@app.route('/user', methods=['GET','POST'])
def user():
    if request.method == "GET":
        return render_template("showoneuser.html")
    if request.method == 'POST':
        usrid = request.form['usr_id']
        user=  UserInfo.query.get(usrid)
        print(user)
        if user == None:
            return render_template("Error.html", Error="No user with such id")

        return render_template("userpage.html",user=user)



@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/calc', methods=['POST', 'GET'])
def calc():
    if request.method == "POST":
        number1 = request.form['number1']
        number2 = request.form['number2']
        oper = request.form['oper']
        return render_template("calc.html", result=calculator(number1, number2, oper), num1=number1, num2=number2,
                               op=oper)

    else:
        return render_template("calc.html")


@app.route('/reg', methods=['POST', 'GET'])
def reg():
    if request.method == "POST":
        log = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']

        new_user = UserInfo(Login=log, Name=name, email=email, Password=password)
        try:

            db.session.add(new_user)
            db.session.commit()

            return redirect('/home')
        except:
            return render_template("Error.html", Error="Can`t write data to db")
    else:
        return render_template("regis.html")
