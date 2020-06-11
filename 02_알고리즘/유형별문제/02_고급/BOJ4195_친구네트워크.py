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


# 뭐징...?
