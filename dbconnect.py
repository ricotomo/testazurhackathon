from flask import Flask
import MySQLdb
from flask_mysqldb import MySQLdb

def connection():
    conn = mySQLdb.connect(host="localhost",
    user="root", passwd = "ricotomo", db = "hackathon")

    c = conn.cursor() #cursor

    return c, conn

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'ricotomo'
app.config['MYSQL_DB'] = 'hackathon'

mysql = MySQL(app)