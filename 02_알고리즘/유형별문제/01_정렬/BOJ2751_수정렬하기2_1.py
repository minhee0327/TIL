import sys


def merge(left, right):
    lp, rp = 0, 0
    sorted_arr = []

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            sorted_arr.append(left[lp])
            lp += 1
        else:
            sorted_arr.append(right[rp])
            rp += 1

    while lp < len(left):
        sorted_arr.append(left[lp])
        lp += 1

    while rp < len(right):
        sorted_arr.append(right[rp])
        rp += 1

    return sorted_arr


def merged_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merged_sort(arr[:mid])
    right = merged_sort(arr[mid:])

    return merge(left, right)


arr = []

for _ in range(int(sys.stdin.readline())):
    arr.append(int(sys.stdin.readline()))

for i in merged_sort(arr):
    print(i)
