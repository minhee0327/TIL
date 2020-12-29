# List

-   ## List 순회

    -   지그재그 순회

        ```py
        arr = [[0]* n for _ in range(n)]

        arr = [[0]*5 for _ in range(5)]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                # 짝수면 (%2)가 0 이 되면서 원래대로 순회(우측)
                # 홀수길이일때 반대로 돌수있음 전체길이에서 j위치만큼 제외한 거리.
                print(i, j+(len(arr[0])-1-2*j)*(i % 2)) # 어디순회하고있는지 찍은것
                #arr[i][j+(len(arr[0])-1-2*j)*(i % 2)]  # 순회중인 값.
        ```

    -   델타이용 2차탐색 (방향벡터 이용방법)
    -   전치행렬
        -   행,렬값이 반대인 행렬
        ```py
        for i in range(3):
            for j in range(3):
                # 절반만 SWAP하기!!(전체 SWAP하게되면 두번 SWAP한거니까 원래대로 돌아옴!!)
                if i <j:
                    arr[i][j]. arr[j][i] = arr[j][i] , arr[i][j]
        ```
    -   zip함수: 동일한 개수로 이루어진 자료형을 묶어주는 역할
        -   `zip(lst, idx)`
        ```py
        lst =['a','b','c']
        idx= [1,2,3]
        zip_res = list(zip(lst,idx))
        print(zip_res) # [('a', 1), ('b', 2), ('c', 3)]
        ```
        ```py
        arr = [[1,2,3], [4,5,6], [7,8,9]]
        print(list(zip(*arr)))
        # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        ```
    -   인덱스

        -   데이터 처리에서 유래
        -   원본데이터에 데이터가 삽입될 경우보다, 상대적으로 크기가 작은 인덱스 List를 정렬하기 때문에 속도가 빨라진다.

    -   선택정렬(selection sort)
        -   주어진 자료들 중 가장 작은 값의 원소부터 차례로 선택해서 위치교환
        -   주어진 list중 최소값을 찾아서 list의 맨 앞에 위치한 값과 교환
        -   맨 처음 위치를 제외한 나머지 list 대상으로 위 과정 반복
