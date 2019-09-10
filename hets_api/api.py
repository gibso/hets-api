from flask import Blueprint, request
from flask_api import status
from hets_api.processor import Processor

bp = Blueprint('generator', __name__, url_prefix='/generator')


@bp.route('/th', methods=['POST'])
def generate_th_files():
    return process_files('th')


@bp.route('/xml', methods=['POST'])
def generate_xml_files():
    return process_files('xml')


@bp.route('/tptp', methods=['POST'])
def generate_tptp_files():
    input_filestorage = request.files['file']
    processor = Processor(input_filestorage)
    result = processor.process_tptp()
    return respond_process_result(result)


def process_files(output_type):
    input_filestorage = request.files['file']
    processor = Processor(input_filestorage)
    result = processor.process(output_type)
    return respond_process_result(result)


def respond_process_result(result):
    if result.returncode == 0:
        return '', status.HTTP_204_NO_CONTENT
    return result.stdout, status.HTTP_500_INTERNAL_SERVER_ERROR
