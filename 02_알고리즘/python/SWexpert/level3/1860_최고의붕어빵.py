for t in range(1, 1+int(input())):
    # N: 자격을 얻은 사람, M: (초)시간 동안 K: 만들수있는 붕어빵 갯수
    N, M, K = map(int, input().split())
    personal_time = sorted(map(int, input().split()))
    ck = 1

    for i in range(N):
        if (personal_time[i] // M)*K - len(personal_time[: i]) > 0:
            continue
        else:
            ck = 0

    if ck:
        print("#{} {}".format(t, 'Possible'))
    else:
        print("#{} {}".format(t, 'Impossible'))

'''
[Code Review]
- 먼저 각 개인이 온 시간들을 정렬했다.
- 그리고 각 타임을 M으로 나눈뒤 K를 곱해서 그 시간까지 만든 붕어빵 갯수를 계산했고
- 거기에서 앞에 온사람들 붕어빵을 뺐는데도 양수면 가능하단 얘기니까 넘어갔다. (continue)
- 근데 한번이라도 양수가 아닐경우에는 불가능하다는 거니까 ck값을 false로 (0) 바꿔준 다음
- ck에 맞추어서 출력했다.
'''
