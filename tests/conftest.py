import pytest
from hets_api import create_app
import os
import glob


@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'HETS_EXECUTABLE': '/opt/Hets/hets'
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
    fileList = glob.glob(f'/opt/data/*')
    for fileName in fileList:
        os.remove(fileName)
