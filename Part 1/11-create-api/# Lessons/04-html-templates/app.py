'''
  HTML Templates
  1. create views/home.tpl


'''


from bottle import run, route, response, template #
from data import ninjas 


@route("/")
def home():
  # using template
  return template('home', ninjas=ninjas) # add name argument -> ninjas -> we can access it in the template


@route("/api/ninjas")
def get_ninjas():
  response.content_type = "application/json"
  return {"data": ninjas}


if __name__ == '__main__':
  run(host='localhost', port=5000, debug=True, reloader=True) 
