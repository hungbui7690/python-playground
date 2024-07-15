"""
Read UTF-8 text files
- The code in the previous examples works fine with ASCII text files. However, if you’re dealing with other languages such as Japanese, Chinese, and Korean, the text file is not a simple ASCII text file. And it’s likely a UTF-8 file that uses more than just the standard ASCII text characters.

- To open a UTF-8 text file, you need to pass the encoding='utf-8' to the open() function to instruct it to expect UTF-8 characters from the file.

- For the demonstration, you’ll use the following quotes.txt file that contains some quotes in Japanese.

"""

# The following shows how to loop through the quotes.txt file:
with open(".\\playground\\quotes.txt", encoding="utf8") as f:
    for line in f:
        print(line.strip())


"""
  Summary

    - Use the open() function with the 'r' mode to open a text file for reading.
    - Use the read(), readline(), or readlines() method to read a text file.
    - Always close a file after completing reading it using the close() method or the with statement.
    - Use the encoding='utf-8' to read the UTF-8 text file.

"""
