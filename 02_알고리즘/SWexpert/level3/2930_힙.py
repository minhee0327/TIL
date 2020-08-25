import heapq

for t in range(1, 1+ int(input())):
    n = int(input())
    heap = []
    ans = []

    for _ in range(n):
        #입력받은 연산에 따라, 첫번째값 a, 두번째값은 b로. (길이가 하나면 a만 변경)
        instruction = input()
        a , b = 0, 0
        if len(instruction) ==1:
            a = int(instruction)
        else:
            a, b = map(int, instruction.split())
        
        if a == 1:
            heapq.heappush(heap, (-b, b))
        elif a ==2:
            if len(heap) == 0:
                ans.append(-1)
            else:
                ans.append(heapq.heappop(heap)[1])

    print("#{}".format(t),end=" ")
    for i in ans:
        print(i, end=" ")
    print()

    