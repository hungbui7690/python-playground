'''
Continuation of statements
- Python uses a newline character to separate statements. It places each statement on one line.
- However, a long statement can span multiple lines by using the backslash (\) character.

Identifiers
- Identifiers are names that identify variables, functions, modules, classes, and other objects in Python.
- The name of an identifier needs to begin with a letter or underscore (_). The following characters can be alphanumeric or underscore.
- Python identifiers are case-sensitive. For example, the counter and Counter are different identifiers.
- In addition, you cannot use Python keywords for naming identifiers.

'''

# The following example illustrates how to use the backslash (\) character to continue a statement in the second line:
a = True
b = False
c = False

if a and b \
  and c:
    print("Continuation of statements")

