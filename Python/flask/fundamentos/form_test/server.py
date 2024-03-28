from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

# nuestra ruta de índice manejará la representación de nuestro formulario

@app.route('/')
def render_form():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Obteniendo información del formulario...")
    print(request.form)
    print("Nombre: ", request.form['name'])
    print("Email: ", request.form['email'])
    # aquí agregamos dos propiedades a la sesión para almacenar el nombre y el correo electrónico
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    print("Showing the User Info from the Form")
    print(request.form)
    return render_template('show.html', name_on_template=session['name'], email_on_template=session['email'])

if __name__ == '__main__':
    app.run(debug=True)