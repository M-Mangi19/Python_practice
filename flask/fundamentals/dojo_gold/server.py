from flask import Flask, request, render_template, redirect, session
import random

app = Flask(__name__)

app.secret_key = 'when i swing my sword they all choppable'

@app.route('/')
def index():
    if 'gold' and 'message' not in session:
        session ['gold'] = 0
        session ['message'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if 'farm' == request.form ['building']:
        gold_found = random.randint(10, 20)
        session['message'].append(f'You found {gold_found} gold coins!!')
        session['gold'] += gold_found
        print(gold_found)
        return redirect('/')

    if 'cave' == request.form ['building']:
        gold_found = random.randint(5, 10)
        session['message'].append(f'You found {gold_found} gold coins!!')
        session['gold'] += gold_found
        print(gold_found)
        return redirect('/')

    if 'house' == request.form ['building']:
        gold_found = random.randint(2, 5)
        session['message'].append(f'You found {gold_found} gold coins!!')
        session['gold'] += gold_found
        print(gold_found)
        return redirect('/')

    if 'casino' == request.form ['building']:
        gold_found = random.randint(-50, 50)
        session['message'].append(f'You gambled and won {gold_found}')
        session['gold'] += gold_found
        print(gold_found)
        return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)