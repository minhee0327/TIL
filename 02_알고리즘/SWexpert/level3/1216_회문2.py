def findRow(s, arr):
    lst = arr[s]
    for i in range(len(lst)):
        for k in range(i+1):
            temp = ''
            for j in range(len(lst)-i-1, -1, -1):
                temp += lst[j+k]
            if temp == temp[::-1]:
                return len(temp)


def findCol(s, arr):
    lst = [arr[i][s] for i in range(len(arr))]
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
[Code Review]
- 풀어내긴했는데... 속도가 엄청 느릴것 같은 코드..ㅎ(반복문 도대체 몇개여..)
- 그나마, 긴 길이부터 비교해서 만약 회문이 있으면 return 하는 방향으로 짬.

- 일단 각 row, col을 한번씩 돌면서
- 새로운 배열 lst를 만듬.(각 줄에 해당하는 list)
- 거기서 list길이만큼, 시작점(k)로, 길이(j)만큼씩 temp에 해당 단어를 만들어서 회문이 되는지 check했고
- 그래서 결과가 회문이 되면 return 길이

- 그 중 max를 계속 업데이트 해나갔음.

- 다만 코드가 난잡해보여서, 다른 사람 코드를 참조해야할 필요가 있음.
- 추후 좀더 개선해보기.
'''
