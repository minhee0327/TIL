from queue import deque

N = int(input())
card = deque([i for i in range(1, 1+N)])
ans = []

while card:
    if len(card) == 1:
        break
    ans.append(card.popleft())
    card.append(card.popleft())

ans.append(card.popleft())

print(' '.join(map(str, ans)))

'''
- 처음 출력형식 error (card에 한장 남겨둔걸 pop해서 출력했었음)
- ans에 아예 card를 전부 비우고 답을 만들어 출력함(통과)
'''
