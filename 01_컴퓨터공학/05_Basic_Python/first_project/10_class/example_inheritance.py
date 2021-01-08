class Parents:
    father = "hong3"

    def father_name(self):
        print(self.father)

class MySon(Parents): #Parents 클래를 상속받음
    description="귀여운 내 반려동"
    def __init__(self,name, age, kind, distinct, speak):
        self.name = name
        self.age = age
        self.kind = kind
        self.distinct = distinct
        self.speak = speak

    def bark(self):
        print(self.speak)

    # 메소드 오버라이
    def father_name(self):
        print("{}이의 아빠는 {} 입니다 >,.<".format(self.name,self.father))


bokgil = MySon('복길','unknown','unknown','사람을 좋아함','멍멍멍')
chapssal = MySon('찹쌀','20day','mixed','cute','낑낑')
cloud = MySon('구름','6month','mixed','cute','야옹')

bokgil.father_name()
chapssal.father_name()
cloud.father_name()

#print(dir(bokgil))