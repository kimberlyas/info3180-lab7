"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, jsonify
from bs4 import BeautifulSoup
import requests
import urlparse
from imageGetter import get_imageURLS  

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/api/thumbnails', methods=['GET'])
def get_thumbnails():
    # Set URL to grab thumbnail images from
    url = "https://www.amazon.com/dp/B015WXL0C6"
    # Get image URLs
    urls = get_imageURLS(url)
    # Generate JSON output
    if urls:
        err = None
        msg = "Success"
    else:
        err = "Request Error"
        msg = "Failed"
    
    return jsonify(error=err, message=msg,thumbnails=urls)

@app.route('/thumbnails/view')
def view_thumbnails():
    """ Render a page for viewing a list of all thumbnails grabbed """
    return render_template('thumbnails.html')
        

###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to tell the browser not to cache the rendered page.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
