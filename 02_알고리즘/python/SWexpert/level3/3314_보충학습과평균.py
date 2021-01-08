for t in range(1, 1+int(input())):
    score = list(map(int, input().split()))
    for i in range(len(score)):
        if score[i] < 40:
            score[i] =40

    print("#{} {}".format(t, sum(score)//len(score)))