for tc in range(1, 1+int(input())):

    N = int(input())
    arr = []
    cnt = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        pivot = arr[i]
        temp = [a for a in arr]
        temp.remove(pivot)
        for t in temp:
            if (pivot[0] < t[0] and pivot[1] > t[1]) or (pivot[0] > t[0] and pivot[1] < t[1]):
                cnt += 1
    print("#{} {}".format(tc, cnt//2))


'''
엄.. 시간초과 날것같아서 걱정했는데 통과 됬다...!
혹시 더 좋은 방법있는지 찾아보기!!!!
'''
