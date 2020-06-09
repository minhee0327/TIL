'''
* 가변 위치 인자.
    - 가변위치인자를 사용할 때 값이 tuple형태로 전달.
    - tuple은 iterable 객체, 따라서 순회, 인덱스로 조회 가능
    - * 만 붙여 쓰면 됨
    - 관용적으로 args라고 붙여 사용하기도 한다.
* 가변 키워드 인자
    - 가변 키워드 인자는 *이 두개
    - **kwargs
    - kwargs도 관용적으로 쓰
'''
print("-----가변 위치 인자 ------")
def exam_arg(*args):
    print(args)
    print(args[1])
    print(type(args))

exam_arg('test','출력',123)
print("-----가변 키워드 인자 ------")
def exam_arg2(**kwargs):
    print(kwargs)
    print(type(kwargs))

exam_arg2(key="test", word="출력", args=123)