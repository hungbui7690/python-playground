"""
Write Text File

"""

# The following illustrates how to write a string to a text file:
with open(".\\playground\\readme.txt", "w") as f:
    f.write("readme")


"""
  Steps for writing to text files
  - To write to a text file in Python, you follow these steps:

      First, open the text file for writing (or append) using the open() function.
      Second, write to the text file using the write() or writelines() method.
      Third, close the file using the close() method.


  - The following shows the basic syntax of the open() function:

      f = open(file, mode)


  - The open() function accepts many parameters. But you’ll focus on the first two:

      The file parameter specifies the path to the text file that you want to open for writing.
      The mode parameter specifies the mode for which you want to open the text file.


  - For writing to a text file, you use one of the following modes:

      Mode	  Description
      'w'	    Open a text file for writing. If the file exists, the function will truncate all the contents as soon as you open it. If the file doesn’t exist, the function creates a new file.
      'a'	    Open a text file for appending text. If the file exists, the function append contents at the end of the file.
      ‘+’	    Open a text file for updating (both reading & writing).


  - The open() function returns a file object that has two useful methods for writing text to the file: write() and writelines().

      The write() method writes a string to a text file.
      The writelines() method write a list of strings to a file at once.


  - The writelines() method accepts an iterable object, not just a list, so you can pass a tuple of strings, a set of strings, etc., to the writelines() method.

  - To write a line to a text file, you need to manually add a new line character:

      f.write('\n')
      f.writelines('\n')

"""
