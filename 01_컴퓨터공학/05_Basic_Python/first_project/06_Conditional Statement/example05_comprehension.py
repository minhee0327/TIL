# list1 에 1~10 까지 요소를 range를 사용해서 선언해서 담은후
# list2 에 "one", "two", "three"..."ten"을 리스트에 담고
# dictionary comprehension 이용해서 구현

list1 = [i for i in range(1, 10+1)]
list2 = ["one","two","three","four","five","six","seven","eight","nine","ten"]
list_to_dict = {k:v for k,v in zip(list1,list2)}

print(list_to_dict)