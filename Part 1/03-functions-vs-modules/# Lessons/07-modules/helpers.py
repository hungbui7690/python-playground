def add(a, b):
  return a + b

def multiply(a, b):
  return a * b

def main():
  print('hello from inside the main function, in the helpers file')


# if we run this file directly -> __main__ 
# if we run app.py -> helpers
print(__name__) 
if __name__ == "__main__":
  main()