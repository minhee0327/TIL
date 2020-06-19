for _ in range(int(input())):
    F = int(input())
    network = dict()
    for i in range(F):
        ans = []
        A, B = input().split()
        if A not in network and B not in network:
            network[B] = [A]
            network[A] = [B]
        elif A in network and B not in network:
            network[A].append(B)
            network[B] = [A]
        elif A not in network and B in network:
            network[B].append(A)
            network[A] = [B]
        elif A in network and B not in network:
            network[A].append(B)
            network[B].append(A)
        print(network)

# 그래프로 친구 상태를 출력해보았는데, 친구관계가 몇인지 구하는거는 생각이 안난다..ㅠㅠ
# union find .. (다음에 알고리즘 이론강의 다시 듣고 풀어보기로! 해설 전에 한번 더 풀어보기!!)
