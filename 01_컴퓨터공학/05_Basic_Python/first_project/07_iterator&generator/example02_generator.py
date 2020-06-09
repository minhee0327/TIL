'''
generator:
- iterator를 생성해주는 함수
- 메모리를 효율적으로 사용할 수 있다.
    - iterator 는 가지고 있는 모든 요소를 메모리에 저장하기 때문에, iterator의 크기만큼 메모리 사용량이 늘어남.
    - generator는 데이터를 한번에 메모리에 저장하는게 아니라, next()함수를 통해 차례로 접근할 때마다 메모리에 저장
    - generator는 진짜 계산 결과값이 필요하기 전까지 계산하지 않음!!!!

    - database에 접근할 때 사용하면, 시간이 적게 들 수 있다. (시간이 곧 돈이다!!)
    - 따라서 메모리를 효율적으로 사용이 가능하다.
'''
import sys

print(sys.getsizeof([i for i in range(1, 10000+1)]))
print(sys.getsizeof((i for i in range(1, 10000+1))))