
for _ in range(int(input())):
    sentence = list(input().split())
    for i in sentence:
        i = i[::-1]
        print(i, end=" ")
