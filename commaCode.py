def commaCode(someList):
    someList.insert(-1, "and")
    someString = ""

    for i in someList:
        someString += i + ","

    return someString.rstrip(",")


someString = ["Foo", "Bar", "Foes"]

print(commaCode(someString))
