# ******************
# reading files
# ******************


def read_file():
  # open file
  file = open('./playground/characters.txt', 'r') # r: read

  # Method 1: read the file
  content = file.read()
  print(content)


	# Method 2: read file line by line
  lines = file.readlines()
  for line in lines:
    print(line)

  # close the file
  file.close()

  return


def main():
  read_file()
  return


if __name__ == "__main__":
  main()