"""
Current Path
- 2 libs that allow us to do that

"""

import os
from pathlib import Path


# Current Working Directory
print("cwd:               ", os.getcwd())
print("cwd:               ", Path().resolve())

# Directory of the Script Being Run
print("script dir:        ", os.path.dirname(__file__))
print("script dir:        ", Path(__file__).parent.resolve())

# Current File Directory
print("current file path: ", __file__)

# Only File Name
print("base name:         ", os.path.basename(__file__))

# Absolute Path
print("abspath:           ", os.path.abspath(__file__))
print("abs dirname:       ", os.path.dirname(os.path.abspath(__file__)))
