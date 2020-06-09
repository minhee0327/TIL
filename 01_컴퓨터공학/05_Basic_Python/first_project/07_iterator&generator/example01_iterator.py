'''
https://docs.python.org/3/glossary.html#term-iterator
iterator
- 데이터 스트림(연속적인)을 나타내는 객체
- iterator 는 next()메서드로 데이터를 순차적으로 호출 가능
- next()로 데이터를 불러올 수 없을 경우(가장 마지막 데이터인 경우), stopiteration exception 발생

- 그렇다면 iterable한 객체들은 모두 iterator?
    - Nope!
    - iterable 한 객체를 iterator 로 바꾸고 싶다면 iter() 로 감싸주기
    - iterable != iterator
    - iterable 객체는 사용시, 파이썬 내부에서 임시로 iterable 객체를 iterator로 자동 변환해서, 반복문을 돌아준 것!

'''
x_list = [1,2,3,4,5,6,7]
print(x_list)
x_list = iter(x_list)
print(type(x_list))
for _ in range(8):
    print(next(x_list))
