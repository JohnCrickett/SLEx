import cStringIO
from datetime import datetime

from reportlab.pdfgen import canvas


LINE_HEIGHT = 15
VERTICAL_START = 800
HORIZONTAL_CENTRE = 200
HORIZONTAL_RIGHT = 400


def generate_pdf(data):
    """
    Generates a PDF report based on the provided dictionary

    data -- the data to render in the report
    """
    output = cStringIO.StringIO()

    # TODO ths should all use a template and some nice table formatting
    # unfortunately only reportlab is available under Anaconda on Windows
    # and it's horrible for PDF generation and doesn't support HTML to PDF
    p = canvas.Canvas(output)
    vertical_position = VERTICAL_START
    p.drawString(HORIZONTAL_CENTRE, vertical_position, 'The Report')
    p.drawString(HORIZONTAL_RIGHT, vertical_position - 20,
                 'Organisation: ' + data['organization'])
    p.drawString(HORIZONTAL_RIGHT, vertical_position - 35, 'Reported: ' +
                 datetime.strptime(data['reported_at'],
                                   '%Y-%m-%d').strftime('%d %B %Y'))
    p.drawString(HORIZONTAL_RIGHT, vertical_position - 50, 'Created: ' +
                 datetime.strptime(data['created_at'],
                                   '%Y-%m-%d').strftime('%d %B %Y'))

    y = vertical_position - 95
    for item in data['inventory']:
        p.drawString(HORIZONTAL_CENTRE, y, item['name'] + ': ' + item['price'])
        y -= LINE_HEIGHT
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()
    return pdf_out
