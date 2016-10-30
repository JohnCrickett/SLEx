#SL Exercise
To launch the service run:  
`python reportservice.py`

You can then view thr reports by visiting:
`http://localhost:5000/report/<id>`  
  
The report will be returned in either JSON, XML or PDF based on the HTTP header
  
for example using curl:  
JSON: `curl -i --header "Accept:application/json" http://localhost:5000/report/1`

XML: `curl -i --header "Accept:application/xml" http://localhost:5000/report/1`
 
PDF: `curl -i --header "Accept:application/pdf" http://localhost:5000/report/1`


# Test Setup
Built to use Py.Test, run the full test suite from the root directory using:  
`py.test`

for individual tests use:  
`py.test test/test_<file>.py`

# Build Env/Setup
Built using Python 2.7.12 on Windows using Anaconda  

Packages used are listed in the enclosed requirements.txt