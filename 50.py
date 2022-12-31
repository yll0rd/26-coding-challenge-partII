from random import randint

def getrandomnumbers(n):
    ListOfNumbers = []
    for i in range(0,n):
        ListOfNumbers.append(randint(1,n))
        while ListOfNumbers.count(ListOfNumbers[-1]) != 1:
            ListOfNumbers.pop(-1)
            ListOfNumbers.append(randint(1,n))
    return ListOfNumbers

print(getrandomnumbers(10))
