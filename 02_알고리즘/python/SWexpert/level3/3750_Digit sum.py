def digit_sum(n):
    return sum(int(digit) for digit in str(n))

ans = []

for t in range(1, 1+int(input())):
    n = int(input())
    while n>=10:
        n = digit_sum(n)
    ans.append("#{} {}".format(t, n))

print("\n".join(ans))

'''
[Code Review]
- 파이썬 4초 이내 통과하기 위해서 결과를 ans에 담아 출력해야했다.
- 처음에는 n을 list형태로 받아서 했는데 이것때문에 속도가 느려지는가 싶어서 바로 int로 사용했다.
- digit_sum 함수의 경우에도 처음엔 배열을 하나 만들어서 사용해보고, while문으로 각 자릿수를 더해보기도 했는데 위 코드가 가장 깔끔한 것 같다.
- 나의경우 항상 조건을 항상 설정할때 등호를 자꾸 잊거나 추가하는데, 이 부분에대해 주의가 필요하다.
- 예를들어 2자리수면 10까지 포함시켜야하는데, 포함안시켜서 계속 오류를 뿜뿜했던 것처럼.. 10은 두자리수다...(아놔...ㅠㅠ바본가..?)

- 추가) Digit sum의 경우 programmers 에서 lv1 자릿수더하기 문제와 동일하다고 생각한다. (js로 풀었지만.. )
'''