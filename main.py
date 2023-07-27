from flask import Flask,request,render_template
import pandas as pd
import numpy as np 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sucess.html')

@app.route('/report')
def report():
    return render_template('select_report.html')

@app.route('/add_report')
def add_report():
    return render_template('add_report.html')

@app.route('/print_report')
def print_report():
    return render_template('report.html')


@app.route('/add_student', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
        
        # Full_name,Date_of_birth,Email,Mobile_number,Gender,Militry_id
       # getting input with name = fname in HTML form
       full_name = request.form.get("fname")
       date_of_birth = request.form.get('datebirth')
       email = request.form.get('email')
       mobile_number = request.form.get('mobile_number')
       gender = request.form.get('gender')
       militry_id = request.form.get('militry_id')
       data = {
           'Full_name':[full_name],
           'Date_of_birth':[date_of_birth],
           'Email':[email],
           'Mobile_number':[mobile_number],
           'Gender':[gender],
           'Militry_id':[militry_id]
       }
       df = pd.DataFrame(data)
       df.to_csv('database.csv', mode='a', index=False, header=False)
       
       return render_template('sucess.html')
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)