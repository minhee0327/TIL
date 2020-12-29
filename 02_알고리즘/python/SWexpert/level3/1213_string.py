for _ in range(10):
    t = int(input())
    q = input()
    string = input()

    print("#{} {}".format(t, len(string.split(sep=q))-1))
