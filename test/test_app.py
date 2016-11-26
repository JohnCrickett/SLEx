import json
from lxml import etree, objectify

import env
from reportservice.reportservice import app


def test_app_json():
    client = app.test_client()
    client.testing = True
    response = client.get('/report/1', headers={'Accept': 'application/json'})
    assert response.status_code == 200
    assert len(response.data) > 0
    data = json.loads(response.data)
    assert data['organization'] == 'Dunder Mifflin'


def test_app_xml():
    client = app.test_client()
    client.testing = True
    response = client.get('/report/1', headers={'Accept': 'application/xml'})
    assert response.status_code == 200
    assert len(response.data) > 0

    xml = response.data

    expected_str = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
                    "<report>"
                        "<organization>Dunder Mifflin</organization>"
                        "<reported>2015-04-21</reported>"
                        "<created>2015-04-22</created>"
                        "<items>"
                            "<item>"
                                "<name>paper</name>"
                                "<price>2.00</price>"
                            "</item>"
                            "<item>"
                                "<name>stapler</name>"
                                "<price>5.00</price>"
                            "</item>"
                            "<item>"
                                "<name>printer</name>"
                                "<price>125.00</price>"
                            "</item>"
                            "<item>"
                                "<name>ink</name>"
                                "<price>3000.00</price>"
                            "</item>"
                        "</items>"
                    "</report>")

    print expected_str

    obj1 = objectify.fromstring(expected_str)
    expected = etree.tostring(obj1)
    obj2 = objectify.fromstring(xml)
    actual = etree.tostring(obj2)
    assert expected == actual


def test_app_pdf():
    client = app.test_client()
    client.testing = True
    response = client.get('/report/1', headers={'Accept': 'application/pdf'})
    assert response.status_code == 200
    assert len(response.data) > 0

    pdf = response.data
    assert pdf  # TODO this just verifies we got something,
                # ideally should verify it is a PDF with the expected contents


def test_app_invalid_report():
    client = app.test_client()
    client.testing = True
    response = client.get('/report/0', headers={'Accept': 'application/json'})
    assert response.status_code == 204
