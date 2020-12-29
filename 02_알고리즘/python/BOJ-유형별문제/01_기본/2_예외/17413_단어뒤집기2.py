string = input()

temp, ans, ck = "", "", False

for i in string:
    if i == ' ':
        if not ck:
            ans += temp[::-1] + ' '
            temp = ''
        else:
            ans += ' '
    elif i == '>':
        ck = False
        ans += '>'
    elif i == '<':
        if not ck:
            ck = True
            ans += temp[::-1] + '<'
            temp = ''
    else:
        if ck:
            ans += i
        else:
            temp += i

ans += temp[::-1]
print(ans)

