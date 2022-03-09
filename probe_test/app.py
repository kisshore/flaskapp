from flask import Flask
from flask import request
import json
import requests
import os
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world():
    output="Hello world from method: "+request.method
    return output

@app.route('/live', methods=['GET', 'POST', 'PUT', 'DELETE'])
def live():
    output="Liveness.. "+request.method
    print(output)
    if check("live"):
        return output,200
    else:
        return output,500

@app.route('/ready', methods=['GET', 'POST', 'PUT', 'DELETE'])
def ready():
    output="Readiness.."+request.method
    print(output)
    if check("ready"):
        return output,200
    else:
        return output,500   

@app.route('/startup', methods=['GET', 'POST', 'PUT', 'DELETE'])
def startup():
    output="Startup..."+request.method
    print(output)
    if check("startup"):
        return output,200
    else:
        return output,500

def check(option):
    ncmd = "mkdir "+option+"; cd "+option+";rm -rf probe_test; git clone https://github.com/kisshore/probe_test.git"
    print(ncmd)
    os.system(ncmd)
    cmd = "cd "+option+";cat probe_test/"+option+" | grep PASS"
    print(cmd)
    val=os.system(cmd)
    if val != 0 :
        return False
    else:
        return True
