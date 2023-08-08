from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hello/<string:name>')
def hello(name):
    return f"Hi {name} !"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return f" {num * name} "

if __name__=="__main__":
    app.run(debug=True)