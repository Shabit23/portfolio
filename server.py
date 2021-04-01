from flask import Flask, render_template, url_for, request, redirect
# import sqlite3
import csv

app = Flask(__name__)

# conn = sqlite3.connect('database.db')
# print "Opened database successfully"

# conn.execute('CREATE TABLE students (email TEXT, subject TEXT, message TEXT)')
# print "Table created successfully"
# conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

# def write_to_db(data):
#     with sql.connect("database.db") as con:
#         cur = con.cursor()
#         cur.execute("INSERT INTO students (email,message,subject) 
#                      VALUES (?,?,?)",(data["email"],data["subject"],data["message"]) )
            
#         con.commit()
#         msg = "Record successfully added"      

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            username = data["email"].split('@')[0]
            write_to_csv(data)
            return render_template('thanks.html', username = username)
        except:
            # con.rollback()
            return 'Could not save to database.'
    else:
        return 'Something went wrong.'