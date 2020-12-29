arr = [[0]*5 for _ in range(5)]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        # 짝수면 (%2)가 0 이 되면서 원래대로 순회(우측)
        # 홀수길이일때 반대로 돌수있음 전체길이에서 j위치만큼 제외한 거리.
        print(i, j+(len(arr[0])-1-2*j)*(i % 2))
        arr[i][j+(len(arr[0])-1-2*j)*(i % 2)]
