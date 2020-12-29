def func(lst):
    result = 0
    check = []
    dx, dy = [0, 1, 0, -1, 0], [1, 0, -1, 0, 0]

    for i in lst:
        x = i//n  # row
        y = i % n  # cloumn

        if x == 0 or y == 0 or x == n-1 or y == n-1:  # 외각은 어차피 씨앗 못심으니까 초기 price 반환
            return 3000

        for d in range(5):  # 시앗 심을수 있는 상황에서는 check추가하고, 해당 값을 result에 더해감.
            nx, ny = x + dx[d], y + dy[d]
            check.append((nx, ny))
            result += dan[nx][ny]

    # 다녀온 곳이 씨핫(3) * 칸(5) = 15 칸을 만족하면 해당 result를 반환, 아니면 초기 price반환
    if len(set(check)) == 15:
        return result

    return 3000


n = int(input())
dan = [list(map(int, input().split())) for _ in range(n)]

# 1. 초기 price를 최대로 잡아두고시작
price = 3000

# 2. i, j, k는 각 씨앗이 돌아야하는 정사각형의 크기
for i in range(n*n):
    for j in range(n*n):
        for k in range(n*n):
            lst = [i, j, k]
            # 3. 현재까지 저장된 price정보와, function을 돌고왔을 때 price정보를 비교하여
            # 최소값 넣기
            price = min(price, func(lst))

print(price)

'''
[코드 리뷰]
- 생각이 잘 안나서 참조
- 아이디어는 3개의 씨앗을 돌리면서
- 각 씨앗이 다녀왔고, 다녀온 곳이 15칸이면 반환하고
- 이걸 반복하면서 최소값을 찾는다는 원리는 나왔는데,

- 이걸 구현하는 방법은 생각이 나지 않았음.
- 그래서 강사님 코드를 참조함.
'''
