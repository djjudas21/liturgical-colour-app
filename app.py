"""
A simple app to display the current liturgical colour of the Church of England
"""
from datetime import date
from flask import Flask, request, render_template, send_file
from liturgical_colour.liturgical import liturgical_colour

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def main():
    """
    Return the liturgical colour
    """
    # Get date from datepicker, if set
    f_date = request.form.get("date") or date.today()
    dayinfo = liturgical_colour(f_date)
    longdate = dayinfo['date'].strftime("%A, %-d %B %Y")
    return render_template('template.html', dayinfo=dayinfo, longdate=longdate, shortdate=f_date)

@app.route('/manifest.json')
def serve_manifest():
    """
    Return the PWA manifest.json
    """
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/sw.js')
def serve_sw():
    """
    Return the service worker
    """
    return send_file('sw.js', mimetype='application/javascript')
