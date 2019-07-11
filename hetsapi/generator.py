import subprocess
import os
from flask import Blueprint, request
from flask_api import status

bp = Blueprint('generator', __name__, url_prefix='/generator')

hetsExe='hets-server'

# this endpoint creates for a casl-input-ile th-output-files
@bp.route('/th', methods=['POST'])
def generate_th_files():
    casl_file = request.files['file']
    casl_file.save('/tmp/input.casl')
    return_code = subprocess.call([hetsExe, '--output-types=th', '--output-dir=/data/th/', '/tmp/input.casl'])
    os.remove('/tmp/input.casl')

    if return_code == 0:
        return '', status.HTTP_204_NO_CONTENT
    return '', status.HTTP_500_INTERNAL_SERVER_ERROR

