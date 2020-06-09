def fibo(data):
    if data<=1:
        return data
    else:
        return fibo(data-1)+fibo(data-2)

def fibo2(data):
    fib_list = [0,1]
    for i in range(2, data+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[-1]

print(fibo(5))
print(fibo2(5))

# 예외처리에 많이 쓰임.