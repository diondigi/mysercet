#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/1/22
from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)




# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your brower is %s</p>' % user_agent

if __name__ == '__main__':
    # manager.run()
    app.run(debug=True)



#test part
# test = app.url_map
# print(test)