import hashlib

from pymysql.constants.ER import PASSWORD_NO_MATCH

from eapp.models import Category, Product
from eapp import app

def load_categories():
    return Category.query.all()


def load_products(kw=None, cate_id=None, page = 1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id==int(cate_id))

    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    query = query.slice(start, start + page_size)

    return query.all()

def count_product():
    return Product.query.count()

def authenticate(username, password):
    password = hashlib.md5(password.strip().e)

def get_user_by_id():
    pass