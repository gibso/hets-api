from flask_api import status
import os
import glob

def test_generate_th_files(client):

    remove_output_files()

    # open file as binary
    file = open('/opt/project/tests/tritone_demo.casl', 'rb')
    data = { 'file': file }

    response = client.post('/generator/th', data=data, content_type='multipart/form-data')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Get a list of all the file paths that ends with .th
    fileList = glob.glob('/data/th/*.th')

    # assert that every file was written
    assert len(fileList) == 5
    assert '/data/th/tritone_demo_SemSys.th' in fileList
    assert '/data/th/tritone_demo_Bbmin.th' in fileList
    assert '/data/th/tritone_demo_Chord.th' in fileList
    assert '/data/th/tritone_demo_G7.th' in fileList
    assert '/data/th/tritone_demo_Symbols.th' in fileList


def test_generate_xml_files(client):

    remove_output_files()

    # open file as binary
    file = open('/opt/project/tests/tritone_demo.casl', 'rb')
    data = {'file': file}

    response = client.post('/generator/xml', data=data, content_type='multipart/form-data')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Get a list of all the file paths that ends with .th
    fileList = glob.glob('/data/xml/*.xml')

    # assert that every file was written
    assert len(fileList) == 1
    assert '/data/xml/tritone_demo.xml' in fileList

# remove every file in the output folder
def remove_output_files():
    fileList = glob.glob('/data/th/*.th')
    for fileName in fileList:
        os.remove(fileName)
