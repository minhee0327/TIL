ans = []
for t in range(1, 1 + int(input())):
    L, U, X = map(int, input().split())
    if X<L:
        ans.append("#{} {}".format(t, L-X))
    elif X>U:
        ans.append("#{} {}".format(t, -1))
    else:
        ans.append("#{} {}".format(t, 0))
        
print('\n'.join(ans))