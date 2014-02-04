from flask import Blueprint

bp = Blueprint('board', __name__, url_prefix='/board')


@bp.route('/')
def index():
    return 'index'