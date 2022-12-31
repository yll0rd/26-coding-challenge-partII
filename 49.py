from random import randint

def getrandomnumbers(n):
    ListOfNumbers = []
    for i in range(0,n):
        ListOfNumbers.append(randint(1,n))
        while ListOfNumbers.count(ListOfNumbers[-1]) != 1:
            ListOfNumbers.pop(-1)
            ListOfNumbers.append(randint(1,n))
    return ListOfNumbers

def shufflestr(string):
    string = list(string)
    listOfRandomIndex = getrandomnumbers(len(string))
    NewString = []
    for i in range(len(string)):
        NewString.append(string[listOfRandomIndex[i]-1])
    return ''.join(NewString)

print(shufflestr("My name is Youmbi"))
