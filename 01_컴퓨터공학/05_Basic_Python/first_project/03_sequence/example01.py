# list1 이라는 변수에 1,2,3 할당 후
# list1 요소값을 1,4,3,5 로 바꾸세요
# 바꾼 list1 타입을 튜플로 바꾸고,
# 요소의 값을 다시 1,2,3으로 바꾸려고 시도해 보세요
list1 = [1,2,3]
list1.insert(1,4)
list1.append(5)
list1.remove(2)
print(list1)

list1 = tuple(list1)
print(type(list1))

#tuple 타입은 수정 , 삭제 시 error 발생!
# 수정 삭제 불가능!!