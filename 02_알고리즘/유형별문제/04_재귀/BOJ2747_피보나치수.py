# 혹시몰라서 수정해본 결과 => 통과
def fibo(n):
    arr = [0, 1]
    for i in range(n-1):
        arr.append(arr[i]+arr[i+1])
    return arr[-1]


n = int(input())
print(fibo(n))

# (아래) 시간초과
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)


# n = int(input())
# print(fibo(n))
