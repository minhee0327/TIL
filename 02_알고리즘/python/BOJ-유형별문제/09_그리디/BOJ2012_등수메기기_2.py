import sys
N = sys.stdin.readline
arr = sorted(int(N()) for _ in range(int(N())))

ans = sum(abs(i - a) for i, a in enumerate(arr, 1))
print(ans)


# 일단 나는 배열을 3개나 선언을 했는데
# 이분은 배열 없이 바로 코드를 작성하였다.
# 심지어 arr 에 리스트 선언을 sroted함수로 바로...(?)이런식으로도 되는구나
# enumerate를 사용해서 idx 값을 사용
# 예상값과, 만족도의 차이를 배열에 저장하지 않고 합해서 결과 나옴


# 정리
# 배열을 덜 사용할 수 있는 방법이 있으면 사용하자.
# idx를 사용해야할 때 enumerate 함수를 생각해내자.
