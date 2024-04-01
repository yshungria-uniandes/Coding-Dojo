from flask import Flask, render_template, request, redirect

# importar la clase de friend.py
from friend import Friend

app = Flask(__name__)


@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/create_friend', methods=["POST"])
def add_friend_to_db():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"]
    }
    print(data)
    Friend.save(data)
    return redirect('/')

            
if __name__ == "__main__":
    app.run(debug=True)

