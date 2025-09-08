#### building url dynamic web applications using Flask and Jinja templating
from flask import Flask, render_template,request
import pandas as pd


app=Flask(__name__)

@app.route("/")     ##route decorator to tell Flask what URL should trigger our function
def home():
    return "<html><h1 style='color:blue;text-align:center'>Welcome to best Flask Application</h1></html>"

## variable rule 
@app.route('/success/<score>')
def success(score):
    return f"<html><h1 style='color:green;text-align:center'>Your score is: st{score}</h1></html>"

@app.route('/exam/<int:score>')
def exam(score):
    result=""
    if score>=33:
        result="pass"
    else:
        result="fail"
    return f"<html><h1 style='color:green;text-align:center'>You have {result}ed the exam</h1></html>"
results={}
def get_grade(mark):
    if mark >= 80:
        return "A+"
    elif mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "E"
@app.route('/result',methods=['POST','GET'])
def result():
    grade=""
    if request.method=='POST':
        subject_name=request.form.get('subject_name')
        marks=int(request.form.get('marks'))
        results.update({subject_name:marks})
        if results:
            average = sum(results.values()) / len(results)
            xy = get_grade(average)
            grade=xy
        else:
            average = 0
            grade = ""
        return render_template('results.html',results=results,subject_name=subject_name,marks=marks,average=average,grade=grade)
    return render_template('results.html',results=results,average=0,grade=grade)

if __name__ == "__main__":
    app.run(debug=True)
    

