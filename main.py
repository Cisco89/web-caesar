from caesar import rotate_string
from flask import Flask, request, render_template, redirect
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('my-form.html').format('')

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    encrypted_text = rotate_string(text, rot)

    # return '<h1>' + encrypted_text + '</h1>'
    return render_template('my-form.html').format(encrypted_text)

app.run()