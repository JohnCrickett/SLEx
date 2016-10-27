import json

from flask import abort, Flask, jsonify, render_template, request, Response, make_response

from database import Database
from pdfgen import generate_pdf

app = Flask(__name__)
app.config['DB_HOST'] = 'candidate.suade.org'
app.config['DB_NAME'] = 'suade'
app.config['DB_USERNAME'] = 'interview'
app.config['DB_PASSWORD'] = 'LetMeIn'


@app.route('/')
def index():
    """User friendly index page at the root of the server
       guides the user to the reportss
    """
    return render_template('index.html')

@app.route('/report/<id>')
def report(id):
    """
    Generates the report for the provided id

    id -- the report id to generate

    will return JSON, XML or PDF depending on the HTTP header 'Accept' provided
    """
    try:
        id = int(id)
    except ValueError, e:
        abort(400) # bad request

    database = Database(app.config['DB_HOST'],
                        app.config['DB_NAME'],
                        app.config['DB_USERNAME'],
                        app.config['DB_PASSWORD'])

    if database.connect():
        database.execute("select id, type from reports where id = '%d'" % id)
        result = database.fetch_one_row()

        if result is None:
            return 'No such report', 204
        obj = json.loads(result['type'])

        if request.headers['Accept'] == 'application/json':
            response = jsonify(obj)
            response.status_code = 200
            return response
        elif request.headers['Accept'] == 'application/xml':
            xml = render_template('report.xml',
                                  organization = obj['organization'],
                                  created = obj['created_at'],
                                  reported = obj['reported_at'],
                                  items = obj['inventory'])
            return Response(xml, status=200, mimetype='text/xml')
        elif request.headers['Accept'] == 'application/pdf':
            pdf = generate_pdf(obj)
            response = make_response(pdf)
            response.headers['Content-Disposition'] = "attachment; filename='report.pdf"
            response.mimetype = 'application/pdf'
            return response
        else:
            abort(204) # no content for this format
    else:
        abort(503) # service is unavailable




