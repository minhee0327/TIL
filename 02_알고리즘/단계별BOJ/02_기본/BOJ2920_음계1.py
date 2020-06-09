arr = list(input().split(' '))
ascending = True
descending = True

for i in range(1, 8):
    if arr[i-1] < arr[i]:
        descending = False
    elif arr[i-1] > arr[i]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
