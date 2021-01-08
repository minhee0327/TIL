def merge(left, right):
    global ans
    if left[-1] > right[-1]:
        ans += 1

    ret = [0] * (len(left) + len(right))
    lp, rp = 0, 0
    idx = 0

    while lp != len(left) and rp != len(right):
        if left[lp] <= right[rp]:
            ret[idx] = left[lp]
            lp += 1
            idx += 1
        else:
            ret[idx] = right[rp]
            rp += 1
            idx += 1

    while lp != len(left):
        ret[idx] = left[lp]
        lp += 1
        idx += 1

    while rp != len(right):
        ret[idx] = right[rp]
        rp += 1
        idx += 1

    return ret


def merge_split(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2

    left = merge_split(lst[:mid])
    right = merge_split(lst[mid:])

    return merge(left, right)


for t in range(1, 1+int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    merge_sort_result = merge_split(a)

    print("#{} {} {}".format(t, merge_sort_result[N//2], ans))
