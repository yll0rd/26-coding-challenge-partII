def caesarcyph(string,n):
    answer = ""
    for i in range(len(string)):
        s = string[i]
        if s == " ":
            answer += " "
        if s.isupper():
            answer += chr((ord(s) + n-65)%26 + 65)
        if s.islower():
            answer += chr((ord(s) + n-97)%26 + 97)
    return answer

print(caesarcyph("Hello World",2))
