'''
  Static Files
  1. create static/style.css
  2. app.py
  3. views/home.tpl


'''


from bottle import run, route, response, template, static_file #
from data import ninjas 



# @route("/public/<filename:path>") # filename:path -> nested subdirectory
@route("/public/<filename>") 
def send_static(filename):
  return static_file(filename, root="./static")


@route("/")
def home():
  return template('home', ninjas=ninjas)


@route("/api/ninjas")
def get_ninjas():
  response.content_type = "application/json"
  return {"data": ninjas}


if __name__ == '__main__':
  run(host='localhost', port=5000, debug=True, reloader=True) 
