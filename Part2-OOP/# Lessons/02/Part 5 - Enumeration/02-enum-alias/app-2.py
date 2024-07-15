"""
When to use enum aliases

- Enumeration aliases can be helpful in some situations. For example, suppose that you have to deal with API from two different systems. And each system has a different response status doe with the same meaning as shown in the following table:

    System 1	        System 2	    Meaning
    REQUESTING	        PENDING	        The request is in progress
    OK	                FULFILLED	    The request was completed successfully
    NOT_OK	            REJECTED	    The request was failed

- To standardize the status codes from these systems, you can use enumeration aliases as follows:

    Your System	    System 1	System 2	Meaning
    IN_PROGRESS	    REQUESTING	PENDING	    The request is in progress
    SUCCESS	        OK	        FULFILLED	The request was completed successfully
    ERROR	        NOT_OK	    REJECTED	The request was failed

"""

# The following defines the ResponseStatus enumeration with aliases:

from enum import Enum


class ResponseStatus(Enum):
    # in progress
    IN_PROGRESS = 1
    REQUESTING = 1
    PENDING = 1

    # success
    SUCCESS = 2
    OK = 2
    FULFILLED = 2

    # error
    ERROR = 3
    NOT_OK = 3
    REJECTED = 3


# The following compares the response code from system 1 to check if the request was successful or not:
code = "OK"
if ResponseStatus[code] is ResponseStatus.SUCCESS:
    print("The request completed successfully")
# The request completed successfully


# Likewise, you can check the response code from system 2 to see if the request was successful:
code = "FULFILLED"
if ResponseStatus[code] is ResponseStatus.SUCCESS:
    print("The request completed successfully")
# The request completed successfully
