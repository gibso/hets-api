from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/generate-th')
def hello_world():
    return 'Hello, World!'