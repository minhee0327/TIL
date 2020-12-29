for t in range(1, 1 + int(input())):
    N = int(input())
    diff = []

    for _ in range(N):
        fun = int(input())
        if fun - 1:
            # 해당 값에서 1을 뺌으로써, 첫 기준점으로부터 차이를 저장.
            diff.append(int(fun-1))

    for i in diff:
        diff = set(diff)
        # 저장된 차이에서 처음 값을기준으로 2배, 3배, ..배수들을 제외시켜감
        diff -= set(range(i*2, max(diff)+1, i))

    print("#{} {}".format(t, len(diff)))
