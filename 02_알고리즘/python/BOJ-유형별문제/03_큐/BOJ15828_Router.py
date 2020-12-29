import sys
from queue import deque

N = int(sys.stdin.readline())
arr = deque([])

while True:
    packetNum = int(sys.stdin.readline())
    if packetNum == 0:
        arr.popleft()
    elif packetNum == -1:
        break
    elif len(arr) == N:
        continue
    else:
        arr.append(packetNum)

if len(list(arr)) == 0:
    print('empty')
else:
    print(' '.join(map(str, list(arr))))

'''
- 서브테스크에 N에 대해서 명시되있어서 점수차이가 이건가했는데;;
- 속도 차이였...(import sys 달아줘서 바로 해결)
'''
