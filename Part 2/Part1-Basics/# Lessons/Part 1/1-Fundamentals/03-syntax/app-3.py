'''
Keywords
- Some words have special meanings in Python. They are called keywords.
- The following shows the list of keywords in Python:

False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise

'''

import keyword

# To find the current keyword list, you use the following code:
print(keyword.kwlist) 


"""
String literals
- Python uses single quotes (\'), double quotes (\"), triple single quotes (\''') and triple-double quotes (\""") to denote a string literal.
- The string literal need to be surrounded with the same type of quotes. For example, if you use a single quote to start a string literal, you need to use the same single quote to end it.
"""
# The following shows some examples of string literals:
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)


'''
  Summary

      A Python statement ends with a newline character.
      Python uses spaces and indentation to organize its code structure.
      Identifiers are names that identify variables, functions, modules, classes, etc. in Python.
      Comments describe why the code works. They are ignored by the Python interpreter.
      Use the single quote, double-quotes, triple-quotes, or triple double-quotes to denote
'''