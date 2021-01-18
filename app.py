from flask import Flask


# app instance
app = Flask(__name__)

# routes
@app.route('/')
def index():
    return '<h1>Hola Mundo</h1>'

@app.route('/user/<name>')
def user(name):

# start
if __name__ == '__main__':
    app.run(debug=True)