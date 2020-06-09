scale = [i for i in range(1, 9)]  # 음계
arr = list(map(int, input().split()))  # 입력값

if arr == scale:
    print("ascending")
elif arr == list(reversed(scale)):
    print("descending")
else:
    print("mixed")
