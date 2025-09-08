from flask import Flask, render_template
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

@app.route("/")     ##route decorator to tell Flask what URL should trigger our function
def home():
    return "Welcome to best Flask Application"


##entry point of the application

if __name__ == "__main__":
    app.run(debug=True)