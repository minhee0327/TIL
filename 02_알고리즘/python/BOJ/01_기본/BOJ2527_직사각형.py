for _ in range(4):
    x1, y1, x2, y2, xx1, yy1, xx2, yy2 = map(int, input().split())
    # 꼭지점 겹치는경우
    if ((x2 == xx1 and y2 == yy1) or (x1 == xx2 and y2 == yy1) or (x2 == xx1 and y1 == yy2) or (x1 == xx2 and y1 == yy2)):
        print("c")
    # 선분이 겹치는 경우
    elif ((x2 == xx1 and y2 != yy1) or (x1 == xx2 and y2 != yy1) or (x2 != xx1 and y1 == yy2) or (x1 != xx2 and y1 == yy2)):
        print("b")
    # 모두 안겹치는경우
    elif (x2 < xx1 or xx2 < x1 or y2 < yy1 or yy2 < y1):
        print("d")
    # 나머지는 서로 면이 겹치는 경우
    else:
        print("a")
