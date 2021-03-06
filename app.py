# import the Flask class from the flask module
from flask import Flask, jsonify, render_template, redirect, url_for, request

from wikidata import get_cities

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('index.html')  # return a string

# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


# access wikidata
@app.route('/api/cities', methods=['GET'])
def cities():
    return jsonify(get_cities())
