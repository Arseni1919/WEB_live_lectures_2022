from flask import Blueprint, render_template

# about blueprint definition
users = Blueprint('users', __name__,
                  static_folder='static',
                  template_folder='templates')


# Routes
@users.route('/users')
def index():
    return render_template('users.html')