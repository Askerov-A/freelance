from flask import Flask
import pathes
import pymongo
import models
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
from routes import front

app = Flask(__name__)
app.register_blueprint(front)

if __name__ == '__main__':
    app.debug = True
    app.run()
