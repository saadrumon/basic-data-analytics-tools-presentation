from typing import KeysView
from flask import Flask, request, abort, jsonify
from flask_restplus import fields, Api, Resource
from functools import wraps
import sqlite3
import os

app_path = os.path.dirname(__file__)
cur = sqlite3.connect(os.path.join(app_path, 'database.db'), check_same_thread=False).cursor() 
cur.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER, userId INTEGER, title TEXT, body TEXT)')

ACCESS_TOKEN = 'accesstoken'

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'access-token'
    }
}

app = Flask(__name__)
api = Api(app=app, authorizations=authorizations, security='apiKey')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'access-token' in request.headers:
            token = request.headers['access-token']
        if not token or token != ACCESS_TOKEN:
            return abort(401, 'Valid Token Required!')
        return f(*args, **kwargs)
    return decorated

posts_api = api.namespace('posts', description='Posts APIs')

posts_model = {
    'id': fields.Integer(required=True),
    'userId': fields.Integer(required=True),
    'title': fields.String(required=True),
    'body': fields.String(required=True)
}

def validate(data):
    for row in data:
        fields = list(row.keys())
        fields.sort()
        if not (fields == ['body', 'id', 'title', 'userId'] 
                and isinstance(row['id'], int) 
                and isinstance(row['userId'], int) 
                and isinstance(row['title'], str) 
                and isinstance(row['body'], str)):
            return False
    return True


@posts_api.route('/')
class Posts(Resource):
    table_name = 'posts'

    @token_required
    def get(self):
        cur.execute('SELECT * FROM posts')
        return jsonify(cur.fetchall())

    @token_required
    @api.expect(api.model(table_name, posts_model))
    def post(self):
        data = request.get_json()
        if not data: abort(404, 'Data not found!')
        if not isinstance(data, list): data = [data]
        sql = None
        if validate(data):
            sql = 'INSERT INTO POSTS (id, userId, title, body) VALUES '
            for row in data:
                sql += f'''({row['id']}, {row['userId']}, "{row['title']}", "{row['body']}")'''
                if row != data[-1]: sql += ', '
            cur.execute(sql)
        return self.get()


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5001, debug=True)
