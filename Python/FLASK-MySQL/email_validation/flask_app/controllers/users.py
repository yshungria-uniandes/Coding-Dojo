from crypt import methods
from flask_app import app
from flask import render_template, redirect, request, flash
from flask_app.models.user import User
# from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    
    email = request.form['email']
    if not email or not User.validate_user(request.form):
        flash("Invalid email address!")
        return redirect('/')
    elif len(email) > 255:
        flash("Email address is too long!")
        return redirect('/')

    elif len(email) < 5:
        flash("Email address is too short!")
        return redirect('/')
    
    User.save(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    all_users= User.get_all()
    return render_template('success.html', all_users= all_users)

@app.route('/delete/<int:id>')
def delete(id):
    data={
        'id': id
    }
    User.delete(data)
    return redirect('/success')