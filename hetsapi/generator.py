import subprocess

from flask import (Blueprint)
from flask_api import status

bp = Blueprint('generator', __name__, url_prefix='/generator')

hetsExe='hets-server'

# this endpoint creates for a casl-input-ile th-output-files
@bp.route('/th')
def generate_th_files():
    return_code = subprocess.call([hetsExe, '--output-types=th', '--output-dir=/data/amalgamation/music/', 'music/tritone_demo.casl'])
    if return_code == 0:
        return '', status.HTTP_204_NO_CONTENT
    return '', status.HTTP_500_INTERNAL_SERVER_ERROR

