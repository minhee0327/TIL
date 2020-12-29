# Linked List

-   ## 리스트 복사
    -   얕은복사
        -   new_lst = old_lst (주소복사)
    -   깊은복사
    -   아래로 내려갈수록 속도 느림
        -   new_lst = old_lst[:] (슬라이싱)
        -   new_lst.extend(old_lst) (리스트 추가)
        -   new_lst = list(old_lst) (list())
        -   new_lst = copy.copy(old_lst) (import copy)
        -   new_lst = [i for i in old_lst] (comprehension)
        -   new_lst = copy.deepcopy(old_lst) (import copy, 가장느림, 리스트의 원소까지 깊은 복사)
