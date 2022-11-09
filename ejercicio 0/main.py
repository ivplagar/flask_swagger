from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'My First Web in Flask!'

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        return 'You are running GET method for '+ user_id + ' user'
    if request.method == 'POST':
        #data = request.form # a multidict containing POST data
        return 'You are running POST method for '+ user_id + ' user ' 
    if request.method == 'DELETE':
        return 'You are running DELETE method for '+ user_id + ' user '


app.run(host='0.0.0.0', port=99)