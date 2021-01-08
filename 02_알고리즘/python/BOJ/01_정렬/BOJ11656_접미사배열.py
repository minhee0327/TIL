S = input()
arr = [S[i:len(S)] for i in range(len(S))]

arr.sort()

for i in arr:
    print(i)
