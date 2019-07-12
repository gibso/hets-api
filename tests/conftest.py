import pytest
from hets_api import create_app
import os
import glob


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True
    })

    remove_all_output_files()
    yield app
    remove_all_output_files()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


def remove_all_output_files():
    remove_output_files('th')
    remove_output_files('xml')


def remove_output_files(file_type):
    fileList = glob.glob(f'/data/{file_type}/*.{file_type}')
    for fileName in fileList:
        os.remove(fileName)
