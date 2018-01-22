#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/1/22
from flask import Flask
from flask import request

app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return '<h1>Hello fan!</h1>'
#
@app.route('/user/<name>')
def user(name):
    return '<h2>Hello,%s</h2>' % name




@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your brower is %s</p>' % user_agent

# if __name__ == '__main__':
#     app.run(debug=True)


#test part
test = app.url_map
print(test)