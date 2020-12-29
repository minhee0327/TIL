# 선택정렬로 구현해보기
N = int(input())
array = list()

for _ in range(N):
    array.append(int(input()))

for i in range(N):
    min_index = i
    for j in range(i+1, N):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

for i in array:
    print(i)

# 기본 정렬 라이브러리로 푼 코드 O(nlogn)
# 선택정렬 코드 O(n²)