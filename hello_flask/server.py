from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return 'Success'

@app.route('/hello/<string:name>/<int:num>')
def hello(name, num):
    return render_template("hello.html", name = name, num = num)

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print (username)
    print(id)
    return "username: " + username + ", id: " + id

if __name__=="__main__":
    app.run(debug=True)










