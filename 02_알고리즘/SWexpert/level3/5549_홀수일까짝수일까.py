ans = []
for t in range(1, 1 + int(input())):
    n = int(input()[-1])
    if n % 2:
        ans.append("#{} {}".format(t, "Odd"))
    else:
        ans.append("#{} {}".format(t, "Even"))

print("\n".join(ans))
