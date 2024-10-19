# https://docs.python.org/3/library/index.html
# print(randint(1,10))
# print(shuffle([1,2,3,4,5,6,7])) # shuffles a list


from random import randint, shuffle

def main():
  number = randint(1, 1000)
  print(f"random number is {number}")

  numbers = [1,2,3,4,5,6,7]
  shuffle(numbers)
  print(f"shuffled numbers: {numbers}")

  return


if __name__ == "__main__":
  main()