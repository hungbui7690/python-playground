'''
  More Routes & Reloader


'''


from bottle import run, route


@route("/")
def home():
    return "Hello World!"


@route("/api/ninjas")
def get_ninjas():
  ninja_data = {
      "name" : "Yoshi",
      "belt_color" : "orange",
      "weapon" : "stick",
      "speed" : "fast"
  }
  message = f"{ninja_data['name']} is a ninja with a {ninja_data['belt_color']} belt and a {ninja_data['weapon']} and is {ninja_data['speed']}"

  return message

# reloader -> similar to nodemon
# Debug Mode is very helpful during early development, but should be switched off for public applications. Keep that in mind.
if __name__ == '__main__':
  run(host='localhost', port=5000, debug=True, reloader=True) 
