"""
TKINTER TEXT

Inserting initial content

    text.insert('1.0', 'This is a Text widget demo')

- The first argument of the insert() method is the position where you want to insert the text.
- The position has the following format:

    'line.column'

- In the above example, ‘1.0’ means line 1, character 0, which is the first character of the first line on the text area.

\\\\\\\\\\\\\\\\\

Retrieving the text value

- To retrieve the contents of a Text widget, you use its get() method. For example:

    text_content = text.get('1.0','end')

- The get() method accepts two arguments. The first argument is the start position, and the second is the end position.
- To retrieve only part of the text, you can specify different start and end positions.

\\\\\\\\\\\\\\\\\\

Disabling the Text widget

- To prevent users from changing the contents of a Text widget, you can disable it by setting the state option to 'disabled' like this:

    text['state'] = 'disabled'

- To re-enable editing, you can change the state option back to normal:

    text['state'] = 'normal'


"""


# To insert contents into the text area, you use the insert() method. For example:

from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert("1.0", "This is a Text widget demo")
# text["state"] = "disabled"

root.mainloop()
