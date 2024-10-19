'''
- file = open(file_name, 'w / w+') 
    -> w: write 
    -> w+: write and read

- though we read the file like below -> it still not show up -> it is because at the time we read, the cursor is at the end of the file

'''


# ******************
# writing data to files
# ******************

characters = ['mario', 'luigi', 'peach', 'bowser']


def write_to_file(file_name):
    # open file -> file not found will be created
    file = open('./playground/characters.txt', 'w+') # w+: write and read

    # write to file
    for c in characters:
        file.write(c + '\n')

    # move the cursor to the beginning of the file
    file.seek(0, 0)

    # read from file
    content = file.read()
    print(content)

    # close the file
    file.close()

    return


def main():
    write_to_file('./playground/characters.txt')
    return


if __name__ == "__main__":
    main()
