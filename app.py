from flask import Flask, render_template
from liturgical_colour.liturgical import liturgical_colour

app = Flask(__name__)

@app.route("/")
def hello_world():
    dayinfo = liturgical_colour(None)
    return render_template('template.html', dayinfo=dayinfo)
