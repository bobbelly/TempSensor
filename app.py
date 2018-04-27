from flask import Flask, render_template
from TempSensor import read_temp
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(index.html)