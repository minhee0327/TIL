def solution(board, moves):
    temp = []
    answer = 0

    for m in moves:
        for b in range(len(board)):
            if board[b][m-1] != 0:
                current = board[b][m-1]
                board[b][m-1] = 0

                if len(temp) == 0:
                    temp.append(current)
                elif len(temp) > 0 and temp[-1] != current:
                    temp.append(current)
                else:
                    answer += 2
                    del temp[-1]
                break
    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
         4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])


'''
1. 카카오 개발 인턴십 2019 문제
    - testcase는 programmers에 있는 거 가져왔음
    - 문제푸는 속도를 조금 더 늘릴수있도록 더 연습을 해야할 것 같다...
'''
