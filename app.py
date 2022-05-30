from flask import Flask, Response,request,jsonify
from time import sleep
import subprocess
import sys, shlex
import os
from flask_cors import CORS, cross_origin
app = Flask(__name__)
#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/")
#@cross_origin()
def helloWorld():
    #def gen():
        #i=0
        #for i in range(1):
            #sleep(1)
        
        #yield(str(os.system("tail -f /var/log/httpd/access.log")))
            #yield str(i)
    return "HELLO"  #Response(gen())
    #return "Hello, cross-origin-world!"
@app.route("/log")
#@cross_origin()
def rr():
    return "HELLO" #Response(helloWorld2())
def helloWorld2():
    process = subprocess.Popen("docker stats",shell=True,stdout=subprocess.PIPE)
    def inner():
        # simulate a long process to watch
        while True:
            output = process.stdout.readline()
            #print(process.poll())
            if process.poll() is not None:
                break
            if output:
                yield output.strip().decode() + '<br/><br/>\n'
    return inner()
@app.route("/subtraction",methods=["POST","GET"])
def subtract():
    args=request.args
    x=int(args.get('x'))
    y=int(args.get('y'))
    result={"first_number":x,"second_number":y,"subtraction":(x-y)}
    return  jsonify(result), {'Content-Type': 'application/json; charset=utf-8'}
app.run(debug=True,port="9000",host="0.0.0.0")

