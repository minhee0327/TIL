from collections import deque

for t in range(1, 1+int(input())):
    N, M = map(int, input().split())

    # pizza_list 담되, 몇번째 index인지도 담기
    pizza_lst = list(map(int, input().split()))
    for i in range(M):
        pizza_lst[i] = [pizza_lst[i], i+1]

    # 빼기 편하게 deque로
    que = deque(pizza_lst[:N])
    pizza_lst = deque(pizza_lst[N:])

    while True:
        # print(que, pizza_lst)
        if len(que) == 1:
            print("#{} {}".format(t, que[0][1]))
            break

        # 화덕에서 꺼낸피자
        outPizza = que.popleft()

        # 화덕에서 꺼낸피자가 0이 아니면 다시넣거나
        # 화덕 자리가 생겼으면서 pizza 남아있으면 넣어주기
        if outPizza[0]//2 != 0:
            que.append([outPizza[0]//2, outPizza[1]])
        elif len(pizza_lst) and len(que) < N:
            que.append(pizza_lst.popleft())
        else:
            continue
