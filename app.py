#Import Flask dependency
from flask import Flask

#Create new Flask app instance
app = Flask(__name__)

#Create Flask route - define the root (starting point)
@app.route('/')
def hello_world():
    return 'Hello world'