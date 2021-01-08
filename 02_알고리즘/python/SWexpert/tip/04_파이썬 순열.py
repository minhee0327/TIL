from itertools import permutations

a = [1, 2, 3]
permute = permutations(a, 2)

print("permutations(lib): ", list(permute))
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]


#####################################
########## 직접 구현하기 ############
####################################


def permutation(arr, r):
    ret = []

    if r > len(arr):
        return ret

    if r == 1:
        for i in arr:
            ret.append([i])

    elif r > 1:
        for i in range(len(arr)):
            temp = [a for a in arr]
            temp.remove(arr[i])

            for p in permutation(temp, r-1):
                ret.append([arr[i]] + p)

    return ret


# print(permutation([1, 2, 3, 4], 3))
print("permutation(func): ", permutation([1, 2, 3], 2))

'''
arr, n = [1,2,3,4], 2의 경우

perm([1,2,3,4], 2) = ([1]+perm([2,3,4],1)) & ([2] + perm([1,3,4], 1)) & ([3] + perm([1,2,4],1)) & ([4] + perm([1,2,3],1))
'''
