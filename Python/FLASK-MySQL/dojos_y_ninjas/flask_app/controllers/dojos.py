from flask_app import app
from flask import render_template, redirect, request, abort
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dashboard():
    return render_template('dojo.html', dojos = Dojo.get_all())

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojo_dashboard(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one(data)
    if dojo:
        return render_template('ninja_show.html', dojo=dojo)
    else:
        abort(404)