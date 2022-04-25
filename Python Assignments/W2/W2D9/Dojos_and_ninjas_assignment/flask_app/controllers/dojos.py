from flask_app import app
from flask import render_template, redirect, request
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
@app.route('/')
def redirect_dojo():
    return redirect('/dojos')

@app.route('/dojos')
def index():
    return render_template("main.html", all_dojos=Dojo.get_all())

@app.route('/show/dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    return render_template("dojo_show.html", dojo=Dojo.get_dojo(data))

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')