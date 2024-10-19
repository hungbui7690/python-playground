# import helpers
from helpers import add, multiply

def main():
  print('hello from inside the main function, in the app file')
  
  # result = helpers.add(2, 7)
  result = add(2, 7)
  print(result)

  result = multiply(3,4)
  print(result)


if __name__ == "__main__":
  main()