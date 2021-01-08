'''
custom error 발생 시, 꼭 Exception을 상속받아서 사용!
'''

class MyError(Exception):
    def __str__(self):
        return "My Cusom Error"

# raise: 강제로 error 발생
try:
    raise MyError()
except Exception as e:
    print(e)