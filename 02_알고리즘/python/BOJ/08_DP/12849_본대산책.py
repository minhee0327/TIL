# 0: 정보과학관
# 1: 전산관
# 2: 미래관
# 3: 신앙관
# 4: 한경직
# 5: 진리관
# 6: 학생회관
# 7: 형남공학관
# 0분에 어떤 지점에 도착할 수 있는 상태
DP = [1, 0, 0, 0, 0, 0, 0, 0, 0]


def nxt(state):
    tmp = [0 for _ in range(8)]
    tmp[0] = state[1] + state[2]
    tmp[1] = state[0] + state[2] + state[3]
    tmp[2] = state[0] + state[1] + state[3] + state[4]
    tmp[3] = state[1] + state[2] + state[4] + state[5]
    tmp[4] = state[2] + state[3] + state[5] + state[7]
    tmp[5] = state[3] + state[4] + state[6]
    tmp[6] = state[5] + state[7]
    tmp[7] = state[4] + state[6]
    for i in range(8):
        tmp[i] %= 1000000007

    return tmp


for d in range(int(input())):
    DP = nxt(DP)

# print(DP[0] % 1000000007)
print(DP[0])

'''
- 출력: 미래정보관(0) 에 돌아왔을 때 경우의 수
- 1000000007로 나누는 이유: int overflow 방지(C) + 답에 대한 해시 값
- C 나 JAVA 라면 연산에 대해 모두 나눠주는게 좋다.(속도)
- 1/10이나 시간이 적게 걸림.
'''
