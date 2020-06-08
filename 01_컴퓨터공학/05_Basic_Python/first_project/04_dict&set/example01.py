# list1 변수에 1~10 요소 담은 리스트 선언
# dict1 변수에 1:1, 2:2:, 11:11, 12:12  라는 요소를 담은 딕셔너리 선언
# list1 과 dict1 키값을 비교하여, dict1 의 키값 중 list1 에 없는 요소들만 추출하여 출력

list1 = [i for i in range(1,11)]
dict1 = {1:1, 2:2, 11:11, 12:12}

for k, v in dict1.items():
    if k not in list1:
        print(v)