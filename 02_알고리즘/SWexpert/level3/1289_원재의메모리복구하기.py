for t in range(1, 1+int(input())):
    default = input()
    cnt = 0

    # 맨 첫자리가 1로 시작하면 반드시 최소 한번 뒤집어야하니까 cnt++
    if int(default[0]):
        cnt += 1
    # 주어진 default의 값에서 앞뒤값이 변화할때만 cnt증가를 시키면 몇번 뒤집힌건지 알수있음
    for i in range(len(default)-1):
        if default[i] != default[i+1]:
            cnt += 1

    print("#{} {}".format(t, cnt))
