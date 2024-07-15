"""
Writing to a UTF-8 text file


"""


# 1) If you write UTF-8 characters to a text file using the code from the previous examples, you’ll get an error like this:
# UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-44: character maps to <undefined>

more_lines = ["竹難難月弓中", "心尸尸難", "大十十木金金難手田尸"]

# with open("readme.txt", "a") as f:
#     f.write("\n".join(more_lines))


# 2) To open a file and write UTF-8 characters to a file, you need to pass the encoding='utf-8' parameter to the open() function.
# The following example shows how to write UTF-8 characters to a text file:
quote = "成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。"

with open(".\\playground\\quotes.txt", "w", encoding="utf-8") as f:
    f.write(quote)


"""
    Summary

        Use the open() function with the w or a mode to open a text file for appending.
        Always close the file after completing writing using the close() method or use the with statement when opening the file.
        Use write() and writelines() methods to write to a text file.
        Pass the encoding='utf-8' to the open() function to write UTF-8 characters into a file.

"""
