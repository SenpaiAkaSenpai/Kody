#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, request
app = Flask(__name__)

print(__name__)

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
@app.after_request
def after_request(response)
    g.db.close()
    return response
    
@app.route("/quiz")
def quiz()
    pytanai = Pytanie.select()
    return render_template('quiz.html', query = pytania)

@app.route("/")
def hello():
    return "<h1>Siema eniu</h1><h2>dobri mudzin</h2>"
    
@app.route("/strona")
def strona():
    return render_template('strona.html')
    
@app.route("/klasa")
def klasa():
    return render_template('klasa.html')


if __name__ == '__main__':
    app.run(debug=True)


