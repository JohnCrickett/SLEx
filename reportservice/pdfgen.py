import cStringIO

from reportlab.pdfgen import canvas
def generate_pdf(data):
    """
    Generates a PDF report based on the provided dictionary

    data -- the data to render in the report
    """
    output = cStringIO.StringIO()

    # TODO ths should all use a template and some nice table formatting
    p = canvas.Canvas(output)
    vertical_position = 800
    p.drawString(200, vertical_position, 'The Report')
    p.drawString(400, vertical_position - 20, 'Organisation: ' + data['organization'])
    p.drawString(400, vertical_position - 35, 'Reported: ' + data['reported_at'])
    p.drawString(400, vertical_position - 50, 'Created: ' + data['created_at'])

    y = vertical_position - 95
    for item in data['inventory']:
        p.drawString(200, y, item['name'] + ': ' + item['price'])
        y -= 15
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()
    return pdf_out
