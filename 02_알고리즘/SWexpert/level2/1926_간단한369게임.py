n = int(input())
count = 0

for i in range(1, n+1):
    count = str(i).count('3') + str(i).count('6')+str(i).count('9')
    if count:
        print('-'*count, end=" ")
    else:
        print(i, end=" ")
