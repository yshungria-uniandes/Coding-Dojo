from flask import Flask, render_template, request, redirect

app = Flask(__name__)

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

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)