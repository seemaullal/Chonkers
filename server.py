from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session
import petfinder


app = Flask(__name__)
#app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage"""
    
    return render_template("homepage.html")

@app.route('/search-results')
def cat_results():
    """Based on user search, display cats"""

    cats = petfinder.search_petfinder()
    # your going to return cats as a json and react will hit this end point
    # to get the returned cats response data

    # for cat in cats['animals']:
    #     cat_id = cat['id']
    #     breed = cat['breeds']['primary']
    #     name = cat['name']
    #     gender = cat['gender']




if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    #connect_to_db(app)
    app.run(port=5000, host='0.0.0.0')
