N = int(input())
score = []

for _ in range(N):
    student, kor, eng, math = map(str, input().split())
    score.append((int(kor), int(eng), int(math), student))

score = sorted(score, key=lambda x: (-x[0], x[1], -x[2], x[3]))

for s in score:
    print(s[3])
