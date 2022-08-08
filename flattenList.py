
# Python program to flatten a nested list
 
# explicit function to flatten a
# nested list
def flattenList(nestedList):
 
    # check if list is empty
    if not(bool(nestedList)):
        return nestedList
 
     # to check instance of list is empty or not
    if isinstance(nestedList[0], list):
 
        # call function with sublist as argument
        return flattenList(*nestedList[:1]) + flattenList(nestedList[1:])
 
    # call function with sublist as argument
    return nestedList[:1] + flattenList(nestedList[1:])