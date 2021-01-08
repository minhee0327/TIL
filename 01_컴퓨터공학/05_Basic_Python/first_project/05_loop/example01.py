# classic 한 문제 :구구단
for i in range(2, 10):
    print("-- {}단 ---".format(i))
    for j in range(1, 10):
        print("{}*{}={}".format(i, j, i*j))
