
from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask('app')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/button/", methods=['GET'])
def button_pressed():
    #Button pressed code
    button_message = "Button Pressed.."
    return render_template('index.html', button_message=button_message);



app.run(host='0.0.0.0', port=8080)
