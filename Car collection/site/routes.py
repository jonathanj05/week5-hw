from flask import Blueprint, render_template

site = Blueprint('site',__name__, template_folder='site_templates')

"""
Blueprint Configuration
The first argument, "site" is the Blueprint's name, 
which is used by Flask's routing system.

The second argument , __name__ is the Blueprint's import name, 
which flask uses to locate the blueprint resources

The last argument, 'template_folder', is the BLueprint's HTML template folder.
Whic tells the BLueprint which HTML files to use for specific routes.
"""

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')