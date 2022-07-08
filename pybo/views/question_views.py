from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')##여기로 받은 질문의 id 값이
def detail(question_id):##함수의 매개변수로 이동
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)