for t in range(1, int(input())+1):
    n = int(input())
    nums = sorted(map(int, input().split()))
    print("#{}".format(t), end=" ")
    for i in nums:
        print(i, end=" ")
    print()
