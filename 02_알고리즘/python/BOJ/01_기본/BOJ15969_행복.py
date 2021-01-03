N = int(input())
score = sorted(map(int, input().split()))

print(score[-1] - score[0])
