"""
Python regular expression functions

- Besides the Pattern class, the re module has some functions that match a string for a pattern:

    match()
    search()
    findall()
    finditer()

- These functions have the same names as the methods of the Pattern object. Also, they take the same arguments as the corresponding methods of the Pattern object. However, you don’t have to manually compile the regular expression before using it.

"""

# The following example shows the same program that uses the findall() function instead of the findall() method of a Pattern object:

import re

s = "Python 3.10 was released on October 04, 2021."
results = re.findall("\d", s)
print(results)


"""
Using the functions in the re module is more concise than the methods of the Pattern object because you don’t have to compile regular expressions manually.

Under the hood, these functions create a Pattern object and call the appropriate method on it. They also store the compiled regular expression in a cache for speed optimization.

It means that if you call the same regular expression from the second time, these functions will not need to recompile the regular expression. Instead, they get the compiled regular expression from the cache.

Should you use the re functions or methods of the Pattern object?

  If you use a regular expression within a loop, the Pattern object may save a few function calls. However, if you use it outside of loops, the difference is very little due to the internal cache.

  The following sections discuss the most commonly used functions in the re module including search(), match(), and fullmatch().

"""
