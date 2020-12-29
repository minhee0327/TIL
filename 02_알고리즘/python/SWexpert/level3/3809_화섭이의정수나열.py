ans = []
for t in range(1, 1+ int(input())):
    n = int(input())
    s = ''
    idx = 0

    while True:
        s+=''.join(list(input().split()))
        if len(s) == n:
            break
    
    while True:
        if str(idx) not in s:
            break
        idx+=1

    ans.append("#{} {}".format(t, idx))

print("\n".join(ans))