arr = list(map(int, input().split()))

if arr == sorted(arr):
    print("ascending")
elif arr == list(reversed(sorted(arr))):
    print("descending")
else:
    print("mixed")
