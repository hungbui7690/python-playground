"""
Variable Scopes
- When you assign an object to a variable, the variable will reference that object in the memory. And it’s saying that the variable is bound to the object.

- After the assignment, you can access the object using the variable name in various parts of your code. However, you cannot access the variable everywhere in the code.

- The variable name and its binding (name and object) only exist in specific parts of your code.

- The part of the code where you define the name/binding is called the lexical scope of the variables.

- Python stores these bindings in something called namespaces. Every scope has its own namespace.

- And you can think that a namespace is a table which contains the label and the reference that the label is bound to.

\\\\\\\\\\\\\\\\\\\\

Global scopes
- The global scope is basically the module scope. The global scope spans a single Python source code file only.

- Python doesn’t have a truly global scope that spans across all modules except for the built-in scope.

- The built-in scope is a special scope that provides globally available objects such as print, len, None, True, and False.

- Basically, the built-in and global variables exist everywhere inside a module.

- Internally, global scopes are nested inside the built-in scope: pic-1

- If you access a variable from a scope and Python doesn’t find it in the namespace of that scope, it’ll search in the enclosing scope’s namespace.

"""

# Suppose that you have the following statement in a module called app.py:
print("Hello")

"""
In this app.py module, Python looks for the print function in the module scope (app.py).

Since Python doesn’t find the definition of the print function in the app.py module scope, Python goes up to the enclosing scope, which is the built-in scope, and looks for the print function there. In this case, it can find the print function in the built-in scope. (pic-2)

If you change the statement to the following, you’ll get an runtime error:
"""

# print(counter)

"""
In this example, Python doesn’t find the counter in the current global scope. Therefore, Python looks for it in the enclosing scope, which is the built-in scope.

However, the variable counter doesn’t exist in the built-in scope. Therefore, Python issues a NameError exception:

      NameError: name 'counter' is not defined
"""
