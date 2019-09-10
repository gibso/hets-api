import subprocess
from flask import current_app as app
import os


class Processor:

    def __init__(self, input_filestorage):
        self.input_filestorage = input_filestorage

    def process_xml(self):
        return self.process('xml')

    def process_th(self):
        return self.process('th')

    def process_tptp(self):
        return self.process('tptp', '--translation=CASL2TPTP_FOF')

    def process(self, output_types, *args):
        return subprocess.run([
            app.config['HETS_EXECUTABLE'],
            *args,
            f'--output-types={output_types}',
            '--output-dir=/data',
            self.input_filepath
        ])

    @property
    def input_filepath(self):
        base_filename = os.path.basename(self.input_filestorage.filename)
        tmp_filepath = f"/tmp/{base_filename}"
        self.input_filestorage.save(tmp_filepath)
        return tmp_filepath
