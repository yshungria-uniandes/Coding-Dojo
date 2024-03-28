from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        session['nombre'] = request.form['nombre']
        session['ubicacion'] = request.form['ubicacion']
        session['lenguaje'] = request.form['lenguaje']
        session['comentario'] = request.form['comentario']
        return redirect(url_for('resultados'))
    return render_template('formulario.html')

@app.route('/result', methods=['GET', 'POST'])
def resultados():
    nombre = session.get('nombre')
    ubicacion = session.get('ubicacion')
    lenguaje = session.get('lenguaje')
    comentario = session.get('comentario')
    return render_template('resultados.html', nombre=nombre, ubicacion=ubicacion, lenguaje=lenguaje, comentario=comentario)

@app.route('/reset_session', methods=['GET'])
def reset_session():
    session.clear()  # Reinicia la sesión
    return redirect(url_for('formulario'))

if __name__ == '__main__':
    app.run(debug=True)
