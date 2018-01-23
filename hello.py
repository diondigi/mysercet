#!/usr/bin/env python
#---coding:utf-8---
#__auther__:Administrator
# date : 2018/1/22
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
# from flask_moment import Moment
# from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [data_required()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
# manager = Manager(app)
# moment = Moment(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    nameForm = NameForm()
    if nameForm.validate_on_submit():
        name = nameForm.name.data
        nameForm.name.data = ''

    return render_template('index.html', form=nameForm, name=name)


# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

@app.errorhandler(404)
def page_net_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_net_found(e):
    return render_template('500.html'), 500





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