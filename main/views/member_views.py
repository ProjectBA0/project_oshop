from flask import Blueprint, redirect, url_for, render_template, g
from .auth_views import login_required
from main import db
from main.models import User   # User 모델을 임포트해야 함

bp = Blueprint('member', __name__, url_prefix='/member')

@bp.route('/mypage', methods=['GET'])
@login_required
def mypage():
    return render_template('member/mypage.html', user=g.user)

@bp.route('/support/')
def support():
    return render_template('support.html')