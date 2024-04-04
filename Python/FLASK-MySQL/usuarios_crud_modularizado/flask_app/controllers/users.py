from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user import User


@app.route("/")
def index():
    users = User.get_all()
    return render_template("mostrar_usuarios.html", users=users)

@app.route("/crear_usuario", methods=["GET", "POST"])
def crear_usuario():
    if request.method == "POST":
        data = {
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
        user_id = User.save(data)
        print(user_id)
        return redirect("/usuario/" + str(user_id))
    else:
        return render_template("crear_usuario.html")

@app.route("/usuario/<int:user_id>")
def leer_usuario(user_id):
    user = User.get_one({"id": user_id})
    return render_template("mostrar_usuario.html", user=user)

@app.route("/usuario/<int:user_id>/editar", methods=["GET", "POST"])
def editar_usuario(user_id):
    if request.method == "POST":
        data = {
            "id": user_id,
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
        }
        User.update(data)
        return redirect("/usuario/" + str(user_id))
    else:
        user = User.get_one({"id": user_id})
        return render_template("editar_usuario.html", user=user)

@app.route("/usuario/<int:user_id>/eliminar")
def eliminar_usuario(user_id):
    User.delete({"id": user_id})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
