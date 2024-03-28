from flask import Flask, session, render_template, redirect, request

app = Flask(__name__)
app.secret_key = 'my secret key'

# ajusta tu código para mostrar el número de veces que el usuario ha visitado la página y el valor del contador, dada la funcionalidad anterior



@app.route('/')
def index():
    print(session)

    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    
    return render_template("contador_vistas.html", visits = session['visits'])


# Agrega una ruta "/destroy_session" que elimine la sesión y redirija a la ruta raíz. Pruébalo.
@app.route('/destroy_session')
def destroy():
    session.clear()
    return render_template("contador_vistas.html", visits = 0)

@app.route('/incrementar_visitas')
def incrementar_visitas():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    
    return render_template("contador_vistas.html", visits = session['visits'])

@app.route('/incrementar_form', methods=['POST'])
def incrementar_form():
    print("Obteniendo información del formulario...")
    print(request.form)

    if 'visits' in session:
        session['visits'] = session.get('visits') + int(request.form['incremento'])
    else:
        session['visits'] = int(request.form['incremento'])

    return redirect('/incrementar_visitas')

# Decodifica la información de las cookies como se muestra en el video
# Ve a la terminal y ejecuta el siguiente comando: Python3 ---------- luego ejecuta los siguientes comandos:
# import base64
# base64.b64decode('eyJ2aXNpdHMiOjEwfQ==')

if __name__ == '__main__':
    app.run(debug=True)