import json
import re
from datetime import datetime
from flask import redirect, render_template, url_for
from flask import Flask
from flask import request
import sqlite3
app=Flask(__name__,template_folder='templates')
app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "Index.html",)

@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/Contact")
def Contact():
    return render_template(
        "contact.html",
        
    )
@app.route("/Feedback")
def Ratings():
    return render_template(
        "ratings5.html",
        
    )
@app.route("/Mainevents")
def MainEvents():
    return render_template(
        "MainEvents.html",
        
    )
@app.route("/about-us-final")
def AboutUS():
    return render_template(
        "about-us-final.html",
        
    )

#Route to login page
@app.route("/Account")
def Account():
    return render_template(
        "lognew.html",
        
    )

@app.route("/Birthdays")
def Birthday():
    return render_template(
        "BirthdayRes.html",
        
    )

@app.route("/Signup")
def signup():
    return render_template(
        "signup.html",
        
    )

@app.route("/Packages")
def Packages():
    return render_template(
        "Packages.html",)

@app.route("/Private Events")
def PrivateEvent():
    return render_template(
        "PrivateEventsRes.html",)

@app.route("/Wedding")
def Wedding():
    return render_template(
        "WeddingRes.html",)


@app.route("/addrec", methods = ['POST', 'GET'])
def addrec():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            fullname=request.form['fullname']
            email=request.form['email']
            phnumber = request.form['phnumber']
            password = request.form['password']
            

            # Connect to SQLite3 database and execute the INSERT
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO newcustomer (fullname, email,phnumber, password) VALUES (?,?,?,?)",(fullname,email,phnumber,password))

                con.commit()
                
                msg = "Signup Successful"
        except sqlite3.IntegrityError:
            msg="Phone number already exists. Please try with new phone number or trying logging into your account"
        except:
            con.rollback()
            msg = "Signup Failed"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('signup.html',msg=msg)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            phone_num = request.form['phonenumber']
            password = request.form['password']
            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM newcustomer WHERE phnumber = ? AND password = ?", (phone_num, password))
                row = cur.fetchone()
                if row:
                    msg = "Login successful"
                    return redirect(url_for('home'))
                    # return render_template("Result.html",msg=msg,link="/login")
                    
                else:
                    msg = "Invalid phone number or password"
        except:
            msg = "Login failed"
        finally:
            con.close()
        return render_template("lognew.html", msg=msg)
    return render_template("lognew.html")


values=[]

#to take values from feedback form

@app.route("/addfed", methods = ['POST', 'GET'])
def addfed():
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        try:
            eventtype=request.form['eventoption']
            ratings=request.form['ratings']
            
            

            # Connect to SQLite3 database and execute the INSERT
            with sqlite3.connect('database.db') as conn:
                print("Connection successful")
                cur = conn.cursor()
                cur.execute("INSERT INTO feedback (eventype, ratings) VALUES (?,?)",(eventtype,ratings))
                print("Inserted data")
                conn.commit()
                
                msg = "Record successfully added to database"
        
        except:
            conn.rollback()
            msg = "Problem with feedback"

        finally:
            conn.close()
            print("Connection closed")
            # Send the transaction message to result.html
        return render_template('ratings5.html',msg=msg)




# # for dynamic chart
# @app.route('/submitfeedback')
# def submitfeedback():
#     conn = sqlite3.connect('database.db')
#     cur = conn.cursor()
#     cur.execute("SELECT eventype, AVG(ratings) FROM feedback GROUP BY eventype")
#     rows = cur.fetchall()
#     labels = [row[0] for row in rows]
#     values = [row[1] for row in rows]
#     conn.close()
#     return render_template('ratings5.html', labels=labels, values=values)
 
# if __name__ == '__main__':
#     app.run(debug=True)
