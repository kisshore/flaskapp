from flask import Flask
from flask import request
import json
import requests
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    output="LATEST VERSION OF CODE : V2"
    return output
