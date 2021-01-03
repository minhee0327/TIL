N = int(input())

tile = [0] * 80
tile[0] = 4
tile[1] = 6

for i in range(2, len(tile)):
    tile[i] = tile[i-1] + tile[i-2]

print(tile[N-1])
