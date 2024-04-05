from flask import Flask, render_template, request, redirect
import burgers_mod.flask_app.models.burger as Burger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create', methods=['POST'])
def create():
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.save(data)
    return redirect('/burgers')

@app.route('/burgers')
def burgers():
    all_burgers = Burger.get_all()
    return render_template("results.html", all_burgers=all_burgers)

@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    data = {'id': burger_id}
    burger = Burger.get_one(data)
    return render_template("details_page.html", burger=burger)

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {'id': burger_id}
    burger = Burger.get_one(data)
    return render_template("edit_page.html", burger=burger)

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {'id': burger_id}
    Burger.destroy(data)
    return redirect('/burgers')

if __name__ == "__main__":
    app.run(debug=True)
