
# importing the flask
from flask import Flask
# Creating the instance of the class the first argument is the  name of the application module or package
app = Flask(__name__) 
# route decorators tells flask which url should trigger  our function
@app.route("/")
# function returning the messages
def home():
    return "web content goes here"

if __name__ == '__main__':
    app.run(debug=True)