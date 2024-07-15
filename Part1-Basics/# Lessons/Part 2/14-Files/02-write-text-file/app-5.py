"""
Appending text files


"""

# To append to a text file, you need to open the text file for appending mode. The following example appends new lines to the readme.txt file:
more_lines = [
    " ",
    "- Forth",
    "- Fifth",
    "- Sixth",
]
with open(".\\playground\\readme.txt", "a") as f:
    f.write("\n".join(more_lines))
