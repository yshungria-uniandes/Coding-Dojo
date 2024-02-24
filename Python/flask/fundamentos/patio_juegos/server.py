# Cuando un usuario visite http://localhost:5000/play, haz que muestre tres cajas azules hermosas. Utiliza una plantilla para renderizar esto. 

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html')


@app.route('/play/<int:x>')
def play_x(x):
    return render_template('play_x.html', x=x)


@app.route('/play/<int:x>/<color>')
def play_x_color(x, color):
    return render_template('play_x_color.html', x=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)