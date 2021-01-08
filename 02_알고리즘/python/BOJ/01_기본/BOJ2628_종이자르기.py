w, h = map(int, input().split())
w, h = [0, w], [0, h]

# 각 지점 (점으로 표시)
for _ in range(int(input())):
    rc, cm = map(int, input().split())
    if rc == 0:
        h.append(cm)
    else:
        w.append(cm)
# 점 크기 순 정렬
w = sorted(w)
h = sorted(h)

# w, h의 최대 길이찾기
w_max, h_max = 0, 0
for i in range(len(w)-1, 0, -1):
    if w[i] - w[i-1] > w_max:
        w_max = w[i] - w[i-1]

for i in range(len(h)-1, 0, -1):
    if h[i] - h[i-1] > h_max:
        h_max = h[i] - h[i-1]

print(w_max * h_max)

'''
[Code Review]
- 먼저 점을 받아서, 가로(0)일때는 세로 점 리스트(h)에 업데이트, 세로일때는 가로점리스트(w)를 업데이트 해나가서 잘려진 점을 받음
- 정렬해서 각 점을 차례대로 둠
- 뒤에서부터 차례로 길이를 구하면서 최대 길이를 구함.(앞에서 부터 해도 상관 없을 것같다.)
- 중간에 break걸려구 뒤에서부터 했는데 구현하면서 생각해보니 앞에 길이가 긴게 나올 수도 있으니까는 앞에서부터 돌아도 될듯
- 그렇게 구해진 가로 세로 최대 길이를 곱해서 최대 넓이를 구함.
'''
