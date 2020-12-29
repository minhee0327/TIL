N = int(input())

input_value = []

for _ in range(N):
    input_value.append(int(input()))

input_value.sort()

for i in input_value:
    print(i)
