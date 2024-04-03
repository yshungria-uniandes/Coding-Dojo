from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    users = User.get_all()
    return render_template("mostrar_usuarios.html", users=users)

@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        data = {
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
        User.save(data)
        return redirect("/")
    else:
        return render_template("crear_usuario.html")

if __name__ == "__main__":
    app.run(debug=True)
