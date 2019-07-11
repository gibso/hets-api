from flask_api import status
import os
import glob

def test_generator_th(client):

    # assert that there are no files at start
    fileList = glob.glob('/data/th/*.th')
    assert len(fileList) == 0

    # open file as binary
    file = open('tritone_demo.casl', 'rb')
    data = { 'file': file }

    response = client.post('/generator/th', data=data, content_type='multipart/form-data')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Get a list of all the file paths that ends with .th
    fileList = glob.glob('/data/th/*.th')

    # assert that every file was written
    assert len(fileList) == 5
    assert fileList[0] == '/data/th/input_SemSys.th'
    assert fileList[1] == '/data/th/input_Bbmin.th'
    assert fileList[2] == '/data/th/input_Chord.th'
    assert fileList[3] == '/data/th/input_G7.th'
    assert fileList[4] == '/data/th/input_Symbols.th'
