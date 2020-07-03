N, A = int(input()), {i: 1 for i in map(int, input().split())}
M = int(input())

for i in list(map(int, input().split())):
    print(A.get(i, 0))

'''
[강사님]
- 해당 값이 있는지 찾는 자료형은 dict, set 이 있다. 
- 그 중 dict를 사용하여, 해당 값이 있을 경우 value를 1로 update한다.
- 그다음 입력받은 값들이 dict에 있으면 해당 value값(1)을 가져오고, 없으면 0 을 출력한다.
- 이때, dict의 get이라는 함수를 사용하면, 없는 값을 찾아올때 default값을 지정해줄 수 있다.
'''
