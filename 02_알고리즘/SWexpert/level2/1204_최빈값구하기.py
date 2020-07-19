from collections import Counter

for _ in range(int(input())):
    t = int(input())

    lst = list(map(int, input().split()))
    lst = sorted(lst, reverse=True)

    cnt = Counter(lst)
    cnt = cnt.most_common()

    print("#{} {}".format(t, cnt[0][0]))
