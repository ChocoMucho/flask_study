from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    ##블루프린트 명칭.등록된 함수명
    ##URL매핑 규칙은 @bp.route('/list/')이므로 => /question + /list/
    return redirect(url_for('question._list'))
