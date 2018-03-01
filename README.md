#Super Quick and Easy Geocoder

#Getting Set Up

First, make sure you have Python 3, virtual environment and pip installed.  If you don't have those, get yourself Homebrew and some google time, then come back.

Clone the repo at `https://github.com/torypayne/geocoder.git`

`cd` into the folder, and then create a Python3 virtual environment. Locally, the command I use to do this is `python3.6 -m venv`

`source env\bin\activate` to activate your virtual environment, and then `pip install -r requirements.txt`

To run the service, `FLASK_APP=app.py flask run` and then direct your browser to http://localhost:5000/.  At this point you can search addresses using the UI.  The response is pure JSON and intentionally unstyled.

You may also geocode addresses directly from the command line using curl. For example, `curl POST http://localhost:5000/geocode?address=1341+valencia+street`.  The service accepts GET requests as well as POST requests, so if you want to share a link with a friend without them needing to worry about making sure it's a post request, you may do so.

The service first checks Google's Geocode service, and then the Here one.

#Design Thoughts

Since the goal of this was to be a quick project (for me) that would be easy to review (for you), I opted to use Flask insted of Django.  My principal thought was that a lightweight framework where all the application and routing logic can be contained in one file was best given the scope of the project.  Typically, I tend to write APIs using the Django REST framework, but that would definitely have been overkill here, given the lack of a database/models/etc.

Enjoy!