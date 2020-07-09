for t in range(1, int(input())+1):
    n = int(input())
    lst = list(map(int, input().split()))
    profit = 0

    while len(lst):
        max_idx = lst.index(max(lst))
        if max_idx == 0:
            lst = lst[max_idx+1:]
        else:
            profit += max(lst) * max_idx - sum(lst[:max_idx])
            if lst == lst[max_idx:]:
                break
            else:
                lst = lst[max_idx+1:]
    print("#{} {}".format(t, profit))


'''
[코드리뷰]
- D2 치곤 좀 어려운 문제 아닌가 싶었다.

- 1.
- 먼저, 최대 매매가가 첫번째 위치에 있다면, 그전에 사서 팔아본다해도 이익이 발생할수가 없다.
- 그래서 그 경우엔 뒤에 lst를 계속 추적해가기로 했다.

- #2.
- 그리고나서 만약 최대 매매가 위치가 첫번째 위치가 아니라면,
- (최대 매매가 * 현재까지 구매한 갯수 - 그전에 구매한것들의 총합)을 계산해줬다.

- 예를들어 3, 5, 9라고 했을때
- 최대 위치(max_idx)가 2이고 9를 매매할수 있는시점에 2개(3,5) 를 구매한 상황이다.
- 이 2개를 9의 값에 팔고, 3,5를 살때 들었던 비용을 빼주면 9를 매매하는 시점의 최대 이익을 계산할 수 있다.

- 최대 매매가 가능했을때 이후에 또 반복해서 사고 팔면서 최대 이익이 발생하는지 체크를 하고
- 반복문을 돌며 가능하면 계속 반복해서 최대이익(profit)을 업데이트 해간다.

- 결과 출력
- 다만 위 코드로는 계속 sample 하나가 error가 난다고 해서 다른 코드를 참조함.
'''
