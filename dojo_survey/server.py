from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)

app.secret_key = 'luminous beings are we, not this crude matter'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    session['your_name'] = request.form['your_name']
    session['dojo_location'] = request.form['dojo_location']
    session['fav_lang'] = request.form['fav_lang']
    session['comments'] = request.form['comments']
    return redirect('/submitted_info')

@app.route('/submitted_info')
def user_info():
    return render_template('user.html')


if __name__=='__main__':
    app.run(debug=True)