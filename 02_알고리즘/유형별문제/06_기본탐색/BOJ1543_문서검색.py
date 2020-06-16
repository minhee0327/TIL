statement = input()
find = input()

idx, count = 0, 0

while idx != len(statement):
    # print(statement[idx:idx+len(find)], find)
    if statement[idx:idx+len(find)] == find:
        count += 1
        idx += len(find)
    else:
        idx += 1

print(count)

'''
1. statement[idx:idx+len(find)]가 같으면 count증가, idx는 찾고자하는 문자길이만큼 증가
2. 다르다면, idx만 한칸씩 움직이면서 확인하기
'''
