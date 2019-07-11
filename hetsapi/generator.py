import subprocess
import os
from flask import Blueprint, request
from flask_api import status

bp = Blueprint('generator', __name__, url_prefix='/generator')

hetsExe='hets-server'

# this endpoint creates for a casl-input-file th-output-files
@bp.route('/th', methods=['POST'])
def generate_th_files():
    casl_file = request.files['file']
    casl_filename = os.path.basename(casl_file.filename)
    tmp_filepath = f"/tmp/{casl_filename}"
    casl_file.save(tmp_filepath)
    return_code = subprocess.call([hetsExe, '--output-types=th', '--output-dir=/data/th/', tmp_filepath])
    os.remove(tmp_filepath)

    if return_code == 0:
        return '', status.HTTP_204_NO_CONTENT
    return '', status.HTTP_500_INTERNAL_SERVER_ERROR


