from flask import Flask, render_template # Importa la clase Flask desde el paquete flask

app = Flask(__name__) # Crea una nueva instancia de la clase Flask llamada "app"

# Localhost:5000/: haz que diga "¡Hola Mundo!"
@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return render_template('index.html', frase="hola", veces=5) # Devuelve la cadena '¡Hola Mundo!' como respuesta

# Localhost:5000/dojo: haz que diga "¡Dojo!"
@app.route('/dojo')
def dojo():
    return '¡Dojo!'

# Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:
# localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
# localhost:5000/say/ Michael: haz que diga "¡Hola, Michael!"
# localhost:5000/say/john: haz que diga "¡Hola, John!"
@app.route('/say/<name>')
def say(name):
    return f'Hola, {name}!'

# Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos (PISTA: int() puede ser útil Por ejemplo, int("35") devuelve 35):
# localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
# localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
# localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces
@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return f'{word} ' * num

@app.route('/list')
def render_list():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    students_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3,1,5], students=students_info)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente 
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

