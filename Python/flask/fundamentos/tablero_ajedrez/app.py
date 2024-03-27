from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tablero/<int:filas>')
def tablero_filas(filas):
    return render_template('tablero_filas.html', filas=filas, columnas=8)

@app.route('/tablero/<int:filas>/<int:columnas>')
def tablero(filas, columnas):
    return render_template('tablero.html', filas=filas, columnas=columnas)

if __name__ == '__main__':
    app.run(debug=True)