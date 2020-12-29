N, r, c = map(int, input().split())

count = 0

while N > 0:
    length = 2**N
    half_len = length//2
    if N == 1:
        if r == 0 and c == 0:
            count += 0
        if r == 0 and c == 1:
            count += 1
        if r == 1 and c == 0:
            count += 2
        if r == 1 and c == 1:
            count += 3
        break

    else:
        if r >= half_len and c >= half_len:
            count += (half_len**2)*3
            r -= half_len
            c -= half_len
        elif r >= half_len:
            count += (half_len**2)*2
            r -= half_len
        elif c >= half_len:
            count += (half_len**2)*1
            c -= half_len
        # print(N, r, c, count)
        N -= 1

print(count)
