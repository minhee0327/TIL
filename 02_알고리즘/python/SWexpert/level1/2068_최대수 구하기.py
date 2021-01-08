import sys

for t in range(int(sys.stdin.readline())):
    lst = list(map(int, input().split()))
    print("#{} {}".format(t, max(lst)))
