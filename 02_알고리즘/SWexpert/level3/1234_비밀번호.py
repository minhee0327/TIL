
for t in range(1, 11):
    N, string = input().split()
    N = int(N)

    string += " "
    while True:
        if string[i] != string[i+1]:
            i += 1
        if len(string) == i or string[i] == " ":
            break
        while string[i] == string[i+1]:
            if len(string) == i:
                break
            string = string[:i] + string[i+2:]
            i -= 1

    print("#{} {}".format(t, string))
