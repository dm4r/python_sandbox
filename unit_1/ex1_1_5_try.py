phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

# Define the search_for person/variable
search_for = "Sam"

# Use the try statement to catch any exceptions to the person being sought
try:
# Either of the below print statements work as expected.  Stack overflow 
# and the Python3 documentation however states best practice is to use
# .format since the use of % can thorw exceptions at times such as the use
# of tuples.  Google for the link.
#   print "This is %s's phone number: %s" % (search_for, phone_book[search_for])
    print "This is {} phone number: {}".format(search_for, phone_book[search_for]) 
except KeyError:
    print "Sorry, we don't have that person on our phone book."
