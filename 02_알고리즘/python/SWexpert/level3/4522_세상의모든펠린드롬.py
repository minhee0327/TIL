# check pattern
def pattern(s):
    mid = len(s)//2
    s = list(s)

    for i in range(mid):
        if s[i] == '?' and s[-1-i] != '?':
            s[-1-i] = '?'
        elif s[i] != '?' and s[-1-i] == '?':
            s[i] = '?'

    return ''.join(s)


# check palindrom
def palindrom(s):
    if s == s[::-1]:
        return True
    return False


ans = []
for t in range(1, 1+int(input())):
    s = input()
    s = pattern(s)

    if palindrom(s):
        ans.append("#{} {}".format(t, "Exist"))
    else:
        ans.append("#{} {}".format(t, "Not exist"))

print('\n'.join(ans))
