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
# 단순히 친구 관계를 합쳐나가는 것으로 생각을 했는데, 그렇게 하면 겹치는 것을 고려해서 제외하지 못하기 때문에
# union - find 구조를 생각해 냈어야 했다.
# 이를 개선하고자, 친구네트워크2py로 다시 풀어보겠다!
# (디버깅!!!!!)
