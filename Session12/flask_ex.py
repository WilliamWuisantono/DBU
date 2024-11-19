# app.py

# Import necessary modules from the Flask package
from flask import Flask, request, redirect, url_for, abort

# Create an instance of the Flask class
app = Flask(__name__)

# --------------------
# Ex1. Exercise 1: URL Building and Redirection
# Objective:
# Create a route /redirect-me that redirects the user to the homepage /. Use the url_for function to build the URL dynamically.
# 
# Instructions:
# 	•	Import the redirect and url_for functions from flask.
# 	•	Define a new route /redirect-me.
# 	•	Inside the view function, use url_for('hello_world') to get the URL for the homepage.
# 	•	Use redirect() to redirect the user to the homepage.
@app.route('/')
def hello_world():
    return 'Hello, World! Welcome to Flask Routing Demo.'

@app.route('/redirect-me')
def redirect_me():
    return redirect(url_for('hello_world'))
# --------------------


# --------------------
# Exercise 2: Exercise: Conditional Redirection Based on User Input
# Objective:
#
# Create a route that accepts user input via query parameters and redirects the user to different pages based on that input.
# http://127.0.0.1:5000/process?choice=dashboard
@app.route('/process')
def process_choice():
    # Retrieve the 'choice' query parameter from the request
    choice = request.args.get('choice')
    
    # Conditional logic to redirect based on the value of 'choice'
    if choice == 'dashboard':
        # Redirect to the 'dashboard' route
        return redirect(url_for('dashboard'))
    elif choice == 'profile':
        # Redirect to the 'profile' route
        return (url_for('profile'))
    else:
        # Redirect to the 'hello_world' route for invalid or missing 'choice'
        return redirect(url_for('home'))
# --------------------


# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    return 'Welcome to your dashboard!'

# Route for the profile page
@app.route('/profile')
def profile():
    return 'This is your profile page.'

# Route for the homepage
@app.route('/')
def home():
    return 'Welcome to the homepage!'

# Checks if the script is run directly (and not imported)
if __name__ == '__main__':
    app.run(debug=True)