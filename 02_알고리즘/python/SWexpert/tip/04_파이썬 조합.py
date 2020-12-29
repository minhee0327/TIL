from itertools import combinations
a = [1, 2, 3]
combi = combinations(a, 2)

print("combinations(lib): ", list(combi))
# [(1,2),(1,3),(2,3)]


def comb(arr, n):
    ret = []

    if n > len(arr):
        return ret

    if n == 1:
        for i in arr:
            ret.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for temp in comb(arr[i+1:], n-1):
                ret.append([arr[i]] + temp)

    return ret


print(comb([1, 2, 3], 2))
# print(comb([1, 2, 3, 4], 2))
'''
arr, n = [1,2,3,4], 2의 경우

comb([1,2,3,4], 2) = ([1]+perm([2,3,4],1)) & ([2] + perm([3,4], 1)) & ([3] + perm([4],1))
'''
