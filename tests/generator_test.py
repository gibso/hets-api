from flask_api import status
import glob


def test_generate_th_files(client):

    # open file as binary
    file = open('tests/assets/tritone_demo.casl', 'rb')
    data = { 'file': file }

    response = client.post('/generator/th', data=data, content_type='multipart/form-data')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Get a list of all the file paths that ends with .th
    file_list = glob.glob('/data/*.th')

    # assert that every file was written
    assert len(file_list) == 5
    assert '/data/tritone_demo_SemSys.th' in file_list
    assert '/data/tritone_demo_Bbmin.th' in file_list
    assert '/data/tritone_demo_Chord.th' in file_list
    assert '/data/tritone_demo_G7.th' in file_list
    assert '/data/tritone_demo_Symbols.th' in file_list


def test_generate_xml_files(client):

    # open file as binary
    file = open('tests/assets/tritone_demo.casl', 'rb')
    data = {'file': file}

    response = client.post('/generator/xml', data=data, content_type='multipart/form-data')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Get a list of all the file paths that ends with .xml
    file_list = glob.glob('/data/*.xml')

    # assert that every file was written
    assert len(file_list) == 1
    assert '/data/tritone_demo.xml' in file_list


def test_generate_tptp_files(client):
    # open file as binary
    file = open('tests/assets/amalgam_tmp.casl', 'rb')
    data = {'file': file}

    response = client.post('/generator/tptp', data=data, content_type='multipart/form-data')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Get a list of all the file paths that ends with .tptp
    file_list = glob.glob('/data/*.tptp')

    # assert that every file was written
    assert len(file_list) == 4
    assert '/data/amalgam_tmp_Boat.tptp' in file_list
    assert '/data/amalgam_tmp_Blend_v8__House_0_Boat_0.tptp' in file_list
    assert '/data/amalgam_tmp_House.tptp' in file_list
    assert '/data/amalgam_tmp_Generic.tptp' in file_list
