'''
  Bottle Framework
  - we can use Django or Flask -> heavy
  - Bottle -> alternative -> lightweight
  - https://bottlepy.org/docs/dev/


'''


from bottle import run, route


@route("/")
def home():
    return "Hello World!"


run(host='localhost', port=5000)
# http://localhost:5000
