def total_score(m, f, s):
    return m * 0.35 + f * 0.45 + s * 0.2


score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']


for t in range(1, int(input())+1):
    real_score = []
    n, k = map(int, input().split())
    for _ in range(n):
        m, f, s = map(int, input().split())
        real_score.append(total_score(m, f, s))

    find_score = real_score[k-1]
    real_score = sorted(real_score, reverse=True)

    # (n//10)을 해줘야, 비율에 맞게 점수를 줄수있음. (예 20명일때, 2명씩 점수줄수있게.)
    rank = real_score.index(find_score) // (n//10)
    grade = score[rank]

    print("#{} {}".format(t, grade))
