from itertools import combinations


for t in range(1, 1+int(input())):
    arr = sorted(map(int, input().split()), reverse=True)

    temp = sorted(set(sum(i)
                      for i in list(combinations(arr, 3))), reverse=True)

    print("#{} {}".format(t, temp[4]))


'''
[Code Review]
- tip 폴더 내부에 순열, 조합 review 별도로 참고한 자료 정리
- 라이브러리 사용한 코드 및 직접 순열, 조합 구현해본 코드 참조.

- 입력받은 수들 중 3개의 숫자로 가능한 조합을 구하여 리스트로 만들어 iterable하게 만든후, 반복시킴
- 각 조합의 경우를 모두 더함
- set으로 중복 제거
- 내림차 정렬중 5번째 값 구하기
'''
