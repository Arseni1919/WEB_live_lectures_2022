import asyncio
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, session
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'

# from pages.users.users import users
# app.register_blueprint(users)


@app.route('/try_request')
def try_request_func():
    return request.method


@app.route('/home_page')
@app.route('/home')
@app.route('/')
def hello_func():
    # DB
    found = True

    if found:
        name = 'Stranger'
        return render_template('index.html', name=name, status=True)
    else:
        return render_template('index.html')


@app.route('/about')
def about_func():
    # DO SOMETHING WITH DB
    if 'username' not in session:
        return render_template('about.html')
    else:
        return render_template('about.html',
                               uni='BGU',
                               profile={'name': session['username'],},
                               degrees=['BSc.', 'MSc.'],
                               hobbies=('art', 'programming', 'teaching', 'horses', 'travel', 'music', 'sql'))


@app.route('/catalog', methods=['GET'])
def catalog_func():
    if 'product_type' in request.args:
        product_type = request.args['product_type']
        size = request.args['size']
        return render_template('catalog.html', p_type=product_type, p_size=size)
    return render_template('catalog.html')


@app.route('/login', methods=['GET', 'POST'])
def login_func():

    if request.method == 'POST':
        name = request.form['nickname']
        password = request.form['password']
        # DB
        session['username'] = name

    return render_template('login.html')


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return redirect(url_for('login_func'))


# ------------------------------------------------- #
# -------------------- USERS ---------------------- #
# ------------------------------------------------- #
@app.route('/users')
def users_func():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=query_result)
# ------------------------------------------------- #
# ------------------------------------------------- #


# @app.route('/hide_users')
# def hide_users_func():
#     session['users'] = ''
#     return redirect(url_for('users_func'))


# ------------------------------------------------- #
# ------------------- SELECT ---------------------- #
# ------------------------------------------------- #
# @app.route('/select_users')
# def select_users_func():
#     query = "select * from users"
#     query_result = interact_db(query=query, query_type='fetch')
#     session['users'] = query_result
#     return redirect(url_for('users_func'))


# ------------------------------------------------- #
# ------------------------------------------------- #

@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/users')

# ------------------------------------------------- #
# -------------------- INSERT --------------------- #
# ------------------------------------------------- #
# @app.route('/insert_user', methods=['GET', 'POST'])
# def insert_user():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         # recheck
#         query = "INSERT INTO users(name, email, password) VALUES ('%s', '%s', '%s')" % (name, email, password)
#         interact_db(query=query, query_type='commit')
#     return redirect(url_for('select_users_func'))


# ------------------------------------------------- #
# ------------------------------------------------- #

@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    return redirect('/users')

# ------------------------------------------------- #
# -------------------- DELETE --------------------- #
# ------------------------------------------------- #

# @app.route('/delete_user', methods=['POST'])
# def delete_user():
#     user_id = request.form['id']
#     query = "DELETE FROM users WHERE id='%s';" % user_id
#     interact_db(query, query_type='commit')
#     return redirect(url_for('select_users_func'))


# ------------------------------------------------- #
# ------------------------------------------------- #

if __name__ == '__main__':
    app.run(debug=True)
