from flask import Flask
from liturgical_colour.liturgical import liturgical_colour

app = Flask(__name__)

@app.route("/")
def hello_world():
    dayinfo = str(liturgical_colour(None))
    return f"<p>{dayinfo}</p>"
