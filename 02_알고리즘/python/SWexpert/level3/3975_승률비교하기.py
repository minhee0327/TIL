arr = []

for t in range(1, 1+int(input())):
    A, B, C, D = map(int, input().split())
    result = ''

    if A/B == C/D:
        arr.append('#{} {}'.format(t, 'DRAW'))
    elif A/B > C/D:
        arr.append('#{} {}'.format(t, 'ALICE'))
    elif A/B < C/D:
         arr.append('#{} {}'.format(t, 'BOB'))

print('\n'.join(arr))

'''
.. 입출력할때 print를 반복문마다 작성하는시간이 arr에 담아서 출력하는시간보다 긴가보다..ㅠㅠ
'''