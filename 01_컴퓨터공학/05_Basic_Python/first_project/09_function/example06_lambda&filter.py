'''
filter, lambda, isinstance 내장함수 사용하여
some_list = [1, "1","one",4.567,{1:"one"}]
some_list안에 있는 요소 중 str 객체 요소만 list로 출력

1. filter : 조건에 맞는 값만 필터링하는 함수
2. isinstance:타입일치 여부 확인하는 함수
'''

some_list = [1, "1","one",4.567,{1:"one"}]
ans = list(filter(lambda x:isinstance(x,str), some_list))
print(ans)