string = input()

temp, ck = "", False

for i in string:
    if i == ' ':
        if not ck:
            print(temp[::-1], end=" ")
            temp = ''
        else:
            print(" ", end="")
    elif i == '>':
        ck = False
        print('>', end="")
    elif i == '<':
        if not ck:
            ck = True
            print(temp[::-1] + '<', end="")
            temp = ''
    else:
        if ck:
            print(i, end="")
        else:
            temp += i

print(temp[::-1], end=" ")
