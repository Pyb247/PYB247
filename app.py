import requests
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
app.secret_key = "super-super-secret-key-faltu-by-nero"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<serv>")
def page(serv):
    return render_template(str(serv)+".html")