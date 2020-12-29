T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a> b:
        print("#{} >".format(test_case))
    elif a==b:
        print("#{} =".format(test_case))
    else:
    	print("#{} <".format(test_case))
