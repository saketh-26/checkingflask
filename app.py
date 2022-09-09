import flask
#creates the Flask application object,which contains data about \
#the application and also methods that tell the application to do
#certain tasks/actions
from flask import Flask,render_template
#print(dir(flask))
app = Flask(__name__)
@app.route('/saketh')
def check():
    return "Hello everyone"
@app.route('/new')
def new():
    return render_template('index.html')
