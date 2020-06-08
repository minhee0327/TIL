# list1 에 1~10 까지 요소를 range를 사용해서 선언해서 담은후
# list2 에 "one", "two", "three"..."ten"을 리스트에 담고
# for 문을 이용해 딕셔너리로 만들어보세요

list1 = []
list2 = ["one","two","three","four","five","six","seven","eight","nine","ten"]
for i in range(1, 11):
    list1.append(i)

ans = dict(zip(list1, list2))
print(ans)