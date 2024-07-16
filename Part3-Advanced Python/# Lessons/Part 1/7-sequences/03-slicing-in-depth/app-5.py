"""
The step value

- Slices support the third argument, which is the step value. The step value defaults to 1 if you don’t specify it:

      seq[star:stop:step]

- It’s equivalent to:

      s = slice(start, stop, step)
      seq[s]

"""

colors = ["red", "green", "blue", "orange"]

print(colors[0:4:2])  # ['red', 'blue']
