from flask import Blueprint, render_template, abort, jsonify, request
from bson import Binary, Code
from bson.json_util import dumps, CANONICAL_JSON_OPTIONS
import models as db

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'azat':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 401

front = Blueprint('front', __name__,
                        template_folder='templates')

@front.route('/works', methods=['GET', 'POST'])
@auth.login_required
def work_with_works():
    if request.method == 'GET':
        return dumps(db.getWorks())
    if request.method == 'POST':
        data = request.form
        return dumps(db.addWorks(request.authorization.username, data['header'], data['price'], data['body']))
