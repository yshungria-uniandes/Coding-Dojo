from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

PLACES = {
    'farm': {'min': 10, 'max': 20},
    'cave': {'min': 5, 'max': 10},
    'house': {'min': 2, 'max': 5},
    'casino': {'min': -50, 'max': 50}
}

def reset_game():
    session['gold'] = 0
    session['moves'] = 0
    session['activities'] = []

@app.route('/')
def index():
    if 'gold' not in session:
        reset_game()
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    gold_range = PLACES[building]
    gold = random.randint(gold_range['min'], gold_range['max'])
    session['gold'] += gold
    session['moves'] += 1
    activity = f'Earned {gold} golds from the {building}!'
    if gold < 0:
        activity = f'Entered a casino and lost {-gold} golds...'
    session['activities'].append(activity)

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    reset_game()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
