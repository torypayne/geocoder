# Super Quick and Easy Geocoder

## Getting Set Up

First, make sure you have Python 3, virtual environment and pip installed.  If you don't have those, get yourself Homebrew and some google time, then come back.

Clone the repo at https://github.com/torypayne/geocoder.git

`cd` into the folder, and then create a Python3 virtual environment. Locally, the command I use to do this is `python3.6 -m venv env` but that may change for you depending on how you have your python 3 installed.

To activate your virtual environemt and install dependencies:

```
source env\bin\activate
pip install -r requirements.txt
```

To run the service, use the command:

```
FLASK_APP=app.py flask run
``` 

And then direct your browser to http://localhost:5000/.  At this point you can search addresses using the UI.  The response is pure JSON and intentionally unstyled.

You may also geocode addresses directly from the command line using curl. For example, `curl GET http://localhost:5000/geocode?address=1341+valencia+street`.

The service first checks Google's Geocode service, and then the Here one.

## Design Thoughts

Since the goal of this was to be a quick project (for me) that would be easy to review (for you), I opted to use Flask insted of Django.  My principal thought was that a lightweight framework where all the application and routing logic can be contained in one file was best given the scope of the project.  Typically, I tend to write APIs using the Django REST framework, but that would definitely have been overkill here, given the lack of a database/models/etc.

Enjoy!