# Create a function that takes a List, converts to a String and inserts a "," between each word in the sting.
# Also, the last word in the string is followed by "and"

def commaCode(someList):
    # a string "and" is instered into the list at index -2 
    someList.insert(-1, "and")
    # a var is created to hold the new string
    someString = ""

    for i in someList:
        #for loop takes each element in someList, adds to someString + a ","
        someString += i + ","
        
       #someString is returned and alls on the .rstrip()method to strip the trailing ","
    return someString.rstrip(",")


someString = ["Foo", "Bar","Foes"]

print(commaCode(someString))
# EXPECTED RESULT should be a string of: Foo,Bar,and Foes
