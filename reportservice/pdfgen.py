import cStringIO

from reportlab.pdfgen import canvas
def generate_pdf(data):
    """
    Generates a PDF report based on the provided dictionary

    data -- the data to render in the report
    """
    output = cStringIO.StringIO()

    # TODO ths should all use a template and some nice
    # table formatting
    p = canvas.Canvas(output)
    p.drawString(200, 800, 'The Report')
    p.drawString(400, 780, 'Organisation: ' + data['organization'])
    p.drawString(400, 765, 'Reported: ' + data['reported_at'])
    p.drawString(400, 750, 'Created: ' + data['created_at'])

    y = 750 - 45
    for item in data['inventory']:
        p.drawString(200, y, item['name'] + ': ' + item['price'])
        y -= 15
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()
    return pdf_out
