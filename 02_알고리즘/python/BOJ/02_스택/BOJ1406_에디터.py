import sys

left = list(sys.stdin.readline().strip())
right = []

for _ in range(int(sys.stdin.readline())):
    # ins mean instruction
    ins = list(sys.stdin.readline().split())
    if ins[0] == 'L' and len(left):
        right.append(left.pop())
    elif ins[0] == 'D' and len(right):
        left.append(right.pop())
    elif ins[0] == 'B' and len(left):
        left.pop()
    elif ins[0] == 'P':
        left.append(ins[1])

ans = left + list(reversed(right))
print(''.join(ans))

'''
- 지금 생각나는 건 키로거랑 비슷한방법
- stack만 가지고 모든 글자를 시뮬레이션하는 방법은 시간초과
- 일단 sys.stdin.readline()을 사용해서 통과되는지 확인결과 => 통과
- deque로 right에 있는 list를 관리하면 조금더 빨리 통과할듯;;
'''
