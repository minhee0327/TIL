def solution(arr):
    temp = [i for i in range(1,1+len(arr))]
    arr.sort()
    if arr == temp:
        return True
    elif arr != temp:
        return False