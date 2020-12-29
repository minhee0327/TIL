'''
등비수열 (Geometric sequence)
- n번째 항 찾기
- 초항, 공차, 몇번째항인지 입력받기 (start, diff, n)
- 몇번째인지 count 하기 (cnt)
- cnt 와 n이 동일하면 해당 값 return 
'''


def GP(start, diff, n):
    ans = start
    cnt = 1

    while True:
        ans *= diff
        cnt += 1

        if n == cnt:
            return ans


start = int(input("초항: "))
diff = int(input("공차(공통차이값): "))
n = int(input("몇번째항?: "))

print(n, "번째 항", GP(start, diff, n))
