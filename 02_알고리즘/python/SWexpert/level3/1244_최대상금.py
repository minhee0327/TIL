def dfs(cnt):
    global ans

    if not cnt:
        temp = int(''.join(num))
        if ans < temp:
            ans = temp
        return

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]  # swap (위치 바꿔봄)
            temp_key = ''.join(num)
            # dict.get : (temp_key, cnt-1)이 없으면 default value로 1을 사용.
            # 이 경우에는, 해당 값을 넣어주어야함
            # 또한 해당 위치는 다녀왔기 때문에 0으로 ck해줌
            if visited.get((temp_key, cnt-1), 1):
                visited[(temp_key, cnt-1)] = 0
                dfs(cnt-1)
            num[i], num[j] = num[j], num[i]  # 원상복구


for t in range(1, 1+int(input())):
    ans = -1

    num, max_cnt = input().split()
    num = list(num)
    max_cnt = int(max_cnt)

    visited = {}
    dfs(max_cnt)

    print("#{} {}".format(t, ans))


'''
tc중 통과되지 않는 값이 2개 있어서 다른 사람 코드 참조
- 일단 나는 백트래킹에 대한 생각을 떠올리지 못했음.
- swap을 하는 모든 경우를 고려해서 가지치기를 하되, 
- 이를 dict에 저장하면서 문제 풀기.
'''
