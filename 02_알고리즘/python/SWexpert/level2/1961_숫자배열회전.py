for t in range(1, 1+int(input())):
    n = int(input())
    origin = [list(input().split()) for _ in range(n)]
    # 90도, 180도, 270도 3가지 case만 받을 것이기 때문에
    arr = [[0]*n for i in range(3)]

    # 90도 회전
    for i in range(n):
        temp = ''
        for j in range(n-1, -1, -1):
            temp += origin[j][i]
        arr[0][i] = temp

    # 180도 회전
    for i in range(n):
        temp = ''
        for j in range(n):
            temp += origin[i][j]
        arr[1][i] = temp[::-1]
    arr[1].reverse()

    # 270도 회전
    for i in range(n-1, -1, -1):
        temp = ''
        for j in range(n):
            temp += origin[j][i]
        arr[2][i] = temp
    arr[2].reverse()

    print("#{}".format(t))
    for j in range(n):
        for i in range(3):
            print(arr[i][j], end=" ")
        print()
'''
[Code Review]
1. output이 왜 이렇게 나왔는지 생각하는 시간이 조금 필요했다. (그림그리니까 보였음!)
2. 90도 , 180도, 270 도 회전했을때 arr값을 먼저 출력해서 확인해가며 구현.
3. [[741,852,963], [987,654,321],[369,258,147]] 이렇게 먼저 담고
4. 돌아가면서 출력함.(741, 987, 369, 852, ... 순 출력)
'''
