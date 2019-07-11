import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('generator', __name__, url_prefix='/generator')

# a simple page that says hello
@bp.route('/hello')
def hello():
    return 'Hello, World!'
