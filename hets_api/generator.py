import subprocess
import os
from flask import Blueprint, request
from flask_api import status

bp = Blueprint('generator', __name__, url_prefix='/generator')


@bp.route('/th', methods=['POST'])
def generate_th_files():
    return generate_files('th')


@bp.route('/xml', methods=['POST'])
def generate_xml_files():
    return generate_files('xml')


def generate_files(output_type):
    casl_file = request.files['file']
    tmp_filepath = save_file_to_tmp(casl_file)
    process = subprocess.run(['hets-server', f'--output-types={output_type}', f'--output-dir=/data/{output_type}/', tmp_filepath])
    os.remove(tmp_filepath)

    if process.returncode == 0:
        return '', status.HTTP_204_NO_CONTENT
    return process.stdout, status.HTTP_500_INTERNAL_SERVER_ERROR


def save_file_to_tmp(file):
    base_filename = os.path.basename(file.filename)
    tmp_filepath = f"/tmp/{base_filename}"
    file.save(tmp_filepath)
    return tmp_filepath
