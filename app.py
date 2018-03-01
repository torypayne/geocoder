from flask import Flask, render_template, redirect, request, flash
import urllib.request
import urllib.parse
import json

app = Flask(__name__)
app.secret_key = "there_are_no_secrets_here_because demoing"

def check_here_geocoder(search_text):
    api_call = 'https://geocoder.cit.api.here.com/6.2/geocode.json?app_id=5llamTqtcL26MdJLtcA4&app_code=PC2d0MJlH8BjR0qm8F7j8A&searchtext='\
                +search_text
    with urllib.request.urlopen(api_call) as response:
        return response.read()

def check_google_geocoder(search_text):
    api_call = 'https://maps.googleapis.com/maps/api/geocode/json?address='+search_text+'&key=AIzaSyBMXLuJ5vPRc7UtA9ul-_xdi0492WWUZQ0'
    with urllib.request.urlopen(api_call) as response:
        return response.read()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/geocode", methods=["POST"])
def geocode_address():
    search_text = request.form['address']
    if search_text == '':
        flash("You must enter an address")
        return render_template("index.html")
    search_text = search_text.replace(' ', '%20')
    results = check_google_geocoder(search_text)
    check_status = json.loads(results)
    if check_status["status"] != "OK":
        try:
            results = check_here_geocoder(search_text)
        except:
            results = "Both geocoders failed!"
    return results



if __name__ == "__main__":
    app.run(debug = True)