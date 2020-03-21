from flask import Flask, render_template, json, request, url_for, redirect, flash
import MySQLdb
from flask_mysqldb import MySQL

from werkzeug.security import generate_password_hash, check_password_hash

from dbconnect import connection

app = Flask(__name__)



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ricotomo'
app.config['MYSQL_DB'] = 'hackathon'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #returns dict not tuple


mysql = MySQL(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignup')
def showSignUp():
    return render_template('signup.html')

@app.route('/showLogin',  methods=['GET', 'POST'])
def showLogin():
    if request.method == 'POST':
        details = request.form
        fName = details['fname']
        lName = details['lname']
        #print (fname, lname) #test if data is taken from form
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (fName, lName))
        mysql.connection.commit()
        cur.close()
        return'success'
    return render_template('login.html')

@app.route('/showMap')
def showMap():
    return render_template('map.html')

@app.route('/showProfile')
def showProfile():
    return render_template('profile.html')

@app.route('/showDeliveries')
def showDeliveries():
    return render_template('deliveries.html')

@app.route('/signup',methods=['POST','GET'])
def signUp():
    try:
        c, conn = connection()
        return('okay')
    except Exception as e:
            return (str(e))

if __name__ == "__main__":
    app.run(port=5000)