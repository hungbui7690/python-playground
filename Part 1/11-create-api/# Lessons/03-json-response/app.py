'''
  JSON Response
  1. data.py


'''


from bottle import run, route, response
from data import ninjas 


@route("/")
def home():
    return "Hello World!"


@route("/api/ninjas")
def get_ninjas():
  # json
  response.content_type = "application/json"
  return {"data": ninjas}


if __name__ == '__main__':
  run(host='localhost', port=5000, debug=True, reloader=True) 
