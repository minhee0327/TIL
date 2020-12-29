def findRow(s, arr):
    lst = arr[s]
    return palindrome(lst)


def findCol(s, arr):
    lst = [arr[i][s] for i in range(len(arr))]
    return palindrome(lst)


def palindrome(lst):
    for i in range(len(lst)):
        for k in range(i+1):
            temp = ''
            for j in range(len(lst)-i-1, -1, -1):
                temp += lst[j+k]
            if temp == temp[::-1]:
                return len(temp)


for _ in range(10):
    t = int(input())
    arr = [list(map(str, input())) for i in range(100)]
    res = 1
    for i in range(len(arr)):
        res = max(res, findRow(i, arr), findCol(i, arr))

    print("#{} {}".format(t, res))

'''
회문의 속도를 줄이기위해
좌, 우 반만 비교하는 식으로 코드를 짜도 괜찮을 것 같다.
'''
