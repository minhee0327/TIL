def findValue(s):
    password = ['0001101', '0011001', '0010011', '0111101', '0100011',
                '0110001', '0101111', '0111011', '0110111', '0001011']
    arr = []
    value = 0
    for i in range(0, len(s)-1, 7):
        for idx, v in enumerate(password):
            if v == s[i:i+7]:
                arr.append(idx)

    for i in range(len(arr)):
        if i % 2:
            value += arr[i]
        else:
            value += arr[i]*3
    return (value, sum(arr))


for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ck = 1

    temp = ''
    for i in range(N):
        if int(arr[i]) != 0:
            temp += arr[i]
            break

    end_point = 0
    for i in range(len(temp)):
        if temp[i] == '1':
            end_point = i
            break

    for i in range(end_point):
        string = temp[i: i+56]
        value, print_v = findValue(string)
        if value % 10 == 0 and value:
            ck = 0
            print("#{} {}".format(t, print_v))
            break
    if ck:
        print("#{} {}".format(t, 0))

'''
[Code Review]
- 문제를 이해하는 시간이 상당히 오래걸렸던 문제
- test case도 길다..
- 일단 내가 접근한 방법은 각 열을 돌면서, set으로 해당 열의 길이가 1이 아닌 곳만 추출했다.
- 그다음 맨 앞에부터 ~ 1이 나오는 순간까지 56개의 문자열을 추출해서
- findValue함수를 구현하여 value, sum값을 구했다.
- value는 검증코드 값, print_v(sum)값은 출력할 값이다. 
- 함수는 7개의 문자열을 비교해가며 password에 해당하는 idx를 구했다.
- ..통과는 잘 했지만.. 효율적으로 짠 코드인지는 좀 의문이 든다..ㅠㅠ 다른 분 코드중에 괜찮은 코드를 보면 참조해야겠다.
'''
