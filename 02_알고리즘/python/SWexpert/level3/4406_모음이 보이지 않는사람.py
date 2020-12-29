for t in range(1, 1+int(input())):
    s = input()
    ans = ''
    for i in s:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            ans += i

    print("#{} {}".format(t, ans))


'''
[Code Review]
- 포함여부 사용할때 배열이 아니더라도 'aeiou'이런식으로 사용할 수 있다.
'''
