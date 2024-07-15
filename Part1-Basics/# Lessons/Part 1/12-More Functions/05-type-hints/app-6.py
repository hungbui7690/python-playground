"""
Adding type hints for lists, dictionaries, and sets

- You can use the following built-in types to set the type hints for a list, dictionary, and set:

    list
    dict
    set

"""

# If you type hints in a variable as a list but later assign a dictionary to it, you’ll get an error:

ratings: list = [1, 2, 3]
ratings = {1: "Bad", 2: "average", 3: "Good"}


"""
    - To specify the types of values in the list, dictionary, and sets, you can use type aliases from the typing module:

        Type Alias	    Built-in Type
        List	        list
        Tuple	        tuple
        Dict	        dict
        Set	            set
        Frozenset	    frozenset
        Sequence	    For list, tuple, and any other sequence data type.
        Mapping	        For dictionary (dict), set, frozenset, and any other mapping data type
        ByteString	    bytes, bytearray, and memoryview types.

"""
