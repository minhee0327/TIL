for t in range(1, 1+int(input())):
    D, A, B, F = map(int, input().split())
    print("#{} {}".format(t, D/(A+B)*F))

'''
- A,B의 총 거리 (D)
- A,B는 반대편으로 움직임. 따라서 A와 B의 속력(시간당 움직인 거리)은 (A+B)
- A,B 기차가 양쪽으로 총 거리를 움직이는동안 걸린 시간 = D / (A+B)
- 파리가 이동한 총 거리 = D/(A+B) * F
'''
