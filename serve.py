from bottle import route, run, response
from rbg import generate_bs


@route('/')
def home():
    response.content_type = 'application/json'
    return generate_bs()

run(host='localhost', port=8080, debug=True)
