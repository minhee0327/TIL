S = input()

zero_count = 0
one_count = 0

if int(S[0]) == 0:
    one_count += 1
elif int(S[0]) == 1:
    zero_count += 1

for i in range(1, len(S)):
    if S[i-1] != S[i]:
        if int(S[i]) == 0:
            one_count += 1
        elif int(S[i]) == 1:
            zero_count += 1

print(min(zero_count, one_count))
