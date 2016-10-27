import env
from reportservice.pdfgen import generate_pdf

def test_pdfgen():
    data = {
          "created_at": "2015-04-22",
          "inventory": [
            {
              "name": "paper",
              "price": "2.00"
            },
            {
              "name": "stapler",
              "price": "5.00"
            },
            {
              "name": "printer",
              "price": "125.00"
            },
            {
              "name": "ink",
              "price": "3000.00"
            }
          ],
          "organization": "Dunder Mifflin",
          "reported_at": "2015-04-21"
        }
    out = generate_pdf(data)
    assert out # TODO should validate PDF