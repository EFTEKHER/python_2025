from flask import Flask, render_template,request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
'''
it create an instance of the Flask class. The first argument is the name of the application’s module or package.
which will be your  WSGI (Web Server Gateway Interface) application.
'''
#### WSGI Application
app=Flask(__name__)  

li=[]
@app.route("/")     ##route decorator to tell Flask what URL should trigger our function
def home():
    return "<html><h1 style='color:blue;text-align:center'>Welcome to best Flask Application</h1></html>"
@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')
@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        li.append({'name': name, 'age': age, 'email': email})
        return render_template('form.html', submitted=True, name=name, age=age, email=email, li=li)

    return render_template('form.html', submitted=False, li=li)

    if request.method=='POST':
        name=request.form.get('name')
        age=request.form.get('age')
        email=request.form.get('email')
        li.append({'name':name,'age':age,'email':email})
        return render_template('form.html',name=name,age=age,email=email ,li=li)
    return render_template('form.html')

##entry point of the application

if __name__ == "__main__":
    app.run(debug=True)