from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")

    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')


@app.route('/show')
def show_user():
    print(request.form)
    return render_template('index.html')


    # return render_template('index.html', name_on_template=session['username'],
# email_on_template=session['useremail'])



if __name__ == "__main__":
    app.run(debug=True)



