# writing data to files


more_characters = ["Diddy Kong", "Donkey Kong", "Wario"]


def write_to_file(filename):
  file = open(filename, 'a+') # a: append vs a+: append and read

  for c in more_characters:
    file.write(c + "\n")

  file.close()



def main():
  write_to_file('./playground/characters.txt')


if __name__ == "__main__":
  main()