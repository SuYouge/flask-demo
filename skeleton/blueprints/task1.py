from flask import Blueprint, render_template

task1_bp = Blueprint('task1', __name__)

@task1_bp.route('/task1')
def hello():
    return render_template("task1.html")