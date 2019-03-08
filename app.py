import os

from flask import Flask, flash, render_template, request
from helpers import *

app = Flask(__name__)
app.secret_key = 'dkjkffksks'

@app.route('/', methods=["GET", "POST"])
def index():
	"""Index page"""
	if request.method == "POST":
		msg = request.form.get("textarea")
		img = request.form.get("output_image")
		if msg:
			fbpost(msg, img)
			flash('Successfully posted!')

	return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, unexpected error: {}'.format(e), 404	

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
    app.run()
