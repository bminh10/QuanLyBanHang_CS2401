import math

from flask import render_template, request

from eapp import app, dao


@app.route('/')
def index():
    products = dao.load_products(request.args.get('kw'), cate_id=request.args.get('category_id'))

    page_size = app.config['PAGE_SIZE']


    # kw =
    # if kw:
    #     products = [p for p in products if p['name'].find(kw) >= 0]

    return render_template('index.html',  products=products,
                           pages = math.ceil(dao.count_product()/page_size))

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.context_processor
def common_response():
    return {
        "categories": dao.load_categories()
    }


if __name__ == '__main__':
    with app.app_context():
        from eapp import admin
        app.run(debug=True)
