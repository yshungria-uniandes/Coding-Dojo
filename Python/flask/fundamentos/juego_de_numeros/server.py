from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def iniciar_juego():
    session['numero_secreto'] = random.randint(1, 100)
    session['intentos'] = 0

@app.route('/', methods=['GET', 'POST'])
def juego():
    if 'numero_secreto' not in session and request.form.get('intento') is None:
        iniciar_juego()

    print('Número secreto:', session['numero_secreto'])
    print('Numero ingresado:', request.form.get('intento'))
   

    if request.method == 'POST':
        session['intentos'] += 1
        intento = int(request.form['intento'])
       

        if intento < session['numero_secreto']:
            mensaje = 'Demasiado bajo. Intenta de nuevo.'
        elif intento > session['numero_secreto']:
            mensaje = 'Demasiado alto. Intenta de nuevo.'
        else:
            mensaje = f'¡Felicidades! ¡Has adivinado el número en {session["intentos"]} intentos!'
            return render_template('resultado.html', mensaje=mensaje)

        if session['intentos'] >= 5:
            mensaje = '¡Tú pierdes! Has alcanzado el límite de intentos. El número era {}'.format(session['numero_secreto'])
            iniciar_juego()
            return render_template('juego.html', mensaje=mensaje)
        
        print('Intentos:', session['intentos'])

        return render_template('juego.html', mensaje=mensaje)

    return render_template('juego.html')

@app.route('/jugar_de_nuevo', methods=['GET', 'POST'])
def jugar_de_nuevo():
    iniciar_juego()
    return juego()

if __name__ == '__main__':
    app.run(debug=True)
