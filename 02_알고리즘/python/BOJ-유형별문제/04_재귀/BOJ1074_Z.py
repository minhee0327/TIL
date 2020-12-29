N, r, c = map(int, input().split())
count = 0

while N > 0:
    one_len = 2 ** (N-1)
    if N > 1:
        if r >= one_len and c >= one_len:
            r -= one_len
            c -= one_len
            count += one_len*one_len*3
        elif r >= one_len and c < one_len:
            r -= one_len
            count += one_len*one_len*2
        elif r < one_len and c >= one_len:
            c -= one_len
            count += one_len*one_len*1
    else:
        if r == 0 and c == 1:
            count += 1
        elif r == 1 and c == 0:
            count += 2
        elif r == 1 and c == 1:
            count += 3
    N -= 1

print(count)
