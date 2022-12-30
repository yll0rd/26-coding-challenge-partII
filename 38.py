def asciitostr(li):
    a = 0
    for i in li:
        li[a] = chr(i)
        a += 1
    li = ''.join(li)
    return li

print(asciitostr([89,111,117,109,98,105,32,76,111,114,100,115,111,110]))

