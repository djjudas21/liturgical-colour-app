from flask import Flask, render_template
from liturgical_colour.liturgical import liturgical_colour

app = Flask(__name__)

@app.route("/")
def main():
    dayinfo = liturgical_colour(None)
    longdate = dayinfo['date'].strftime("%A, %-d %B %Y")
    return render_template('template.html', dayinfo=dayinfo, longdate=longdate)
