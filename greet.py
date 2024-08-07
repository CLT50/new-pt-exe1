from flask import Flask
app= Flask(__name__)

@app.route('/welcome')
def show_welcome():
    return f'<h1>"Welcome"</h1>'

@app.route('/welcome/back')
def show_welcome_back():
    return f'<h1>"Welcome Back"</h1>'

@app.route('/welcome/home')
def show_welcome_home():
    return f'<h1>"Welcome Home"</h1>'
