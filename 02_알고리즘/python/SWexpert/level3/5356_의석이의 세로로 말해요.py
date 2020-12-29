import collections

for t in range(1, 1+int(input())):
    arr = [collections.deque(list(input())) for _ in range(5)]
    total_len = sum(len(m) for m in arr)
    ans = ''

    while True:
        if total_len == 0:
            break
        for i in range(5):
            if len(arr[i]):
                ans += arr[i].popleft()
                total_len -= 1

    print("#{} {}".format(t, ans))

'''
처음에는 제일 긴 문자열만큼 배열의 길이를 수정해서 풀까 했는데
빈배열이 안쓰는데 있으면.. 좀 낭비같아서(반복문도 여러번 돌아야할 것 같고..) 
그래서 반복문을 돌때마다 앞에 값을 빼내서 총 문자열 길이만큼 돌면서 답을 구하면 어떨까했다.
pop(0)을 써서 하려다가, 예전에 속도가 뭔가 느렸던거같아서 collections에 deque를 사용해서 구현해보았다.
'''
