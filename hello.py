#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/1/22
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
