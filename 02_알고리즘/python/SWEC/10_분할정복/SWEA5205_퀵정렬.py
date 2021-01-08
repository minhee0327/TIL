def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst)//2]
    left, right, eq = list(), list(), list()

    for i in range(len(lst)):
        if pivot > lst[i]:
            left.append(lst[i])
        elif pivot == lst[i]:
            eq.append(lst[i])
        else:
            right.append(lst[i])

    return quick_sort(left) + eq + quick_sort(right)


for t in range(1, 1+int(input())):
    N = int(input())
    a = list(map(int, input().split()))

    res = quick_sort(a)

    print("#{} {}".format(t, res[N//2]))


'''
- testcase 9개 통과 1개 통과 X(제한시간초과'')
- 어디가 잘못된건지 찾기 어려움...;;
- 일단 두고 담에 찾으면 수정하겠음.
'''
