'''
1~100까지 출력하는 프로그램
1. 3의 배수이면 fizz
2. 5의 배수이면 buzz
3. 15의 배수이면 fizzbuzz

'''
for i in range(1,100+1):
    if i % 3 ==0 and i % 5 == 0:
        print(i,"FizzBuzz")
    elif i%3 == 0:
        print(i,"Fizz")
    elif i%5 == 0:
        print(i,"Buzz")
    else:
        print(i)