#写注释啊，别打错别字啊
from flask import Blueprint

weibo_bp = Blueprint('weibo', __name__, url_prefix='/weibo',
                     template_folder='./templates')


