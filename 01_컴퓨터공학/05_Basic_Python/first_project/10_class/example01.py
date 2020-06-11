# 강의에서는 animal 로 진행
# 책으로 변형해서 생각해보았음!
# typeError:'int' object is not collable => 변수와 함수의 이름이 같을 때 발생하는 에러

class MyBook:
    def __init__(self, title, author, publisher, value, amount):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.value = value
        self.amount = amount

    def price(self):
        print(self.value)

book1 = MyBook('데이터베이스 개론과 실습','박우창','한빛', 25000, 100)
book2 = MyBook('웹프로그래밍','천인국','인피니티북스',30000,50)
book3 = MyBook('코드로배우는 스프링 웹프로젝트','구멍가게 코딩단','남가람북스',19000,30)

book1.price()
book2.price()
book3.price()