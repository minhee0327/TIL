
for t in range(int(input())):
    string = input()
    for i in range(1, 10):
        temp1 = string[:i]
        temp2 = string[i:i*2]
        if temp1 == temp2:
            # print('#', t+1, string.count(temp1)) #해당 마디가 이안에 몇개 있는지
            print("#{} {}".format(t+1, i))
            break
