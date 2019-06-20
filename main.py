from flask import Flask, request, render_template, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('my-form.html')

app.run()