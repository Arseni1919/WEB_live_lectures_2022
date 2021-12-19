import asyncio
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, session

app = Flask(__name__)
app.secret_key = '123'


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
    if session['username'] == '':
        return render_template('about.html')
    else:
        return render_template('about.html',
                               uni='BGU',
                               profile={'name': 'Arseni',
                                        'second_name': 'Perchik',
                                        'middle_name': 'Ariel'},
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


if __name__ == '__main__':
    app.run(debug=True)
