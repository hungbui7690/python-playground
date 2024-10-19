'''
  Post Requests
  - request.json -> similar to req.body
    -> from bottle !== not from "requests" package
  - test: 
    -> test post route
    -> go to http://localhost:5000/api/ninjas to check the response


'''


from bottle import run, route, response, template, static_file, request # 1.
from data import ninjas 


@route("/public/<filename:path>") 
def send_static(filename):
  return static_file(filename, root="./static")


@route("/")
def home():
  return template('home', ninjas=ninjas)


@route("/api/ninjas")
def get_ninjas():
  response.content_type = "application/json"
  return {"data": ninjas}


@route("/api/ninjas", method="POST") # 2. method="POST"
def add_ninja():
  new_ninja = request.json # 3. from bottle

  # in case of error -> use if to check -> otherwise -> no need to check
  if isinstance(new_ninja, dict):
    ninjas.append(new_ninja)

  response.content_type = "application/json"
  return {"message": "Added a new ninja", "data": new_ninja}


if __name__ == '__main__':
  run(host='localhost', port=5000, debug=True, reloader=True) 
