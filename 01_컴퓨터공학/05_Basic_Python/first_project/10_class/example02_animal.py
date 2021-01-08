class Animal:
    description="귀여운 내 반려동"
    def __init__(self,name, age, kind, distinct, speak):
        self.name = name
        self.age = age
        self.kind = kind
        self.distinct = distinct
        self.speak = speak

    def bark(self):
        print(self.speak)

cloud = Animal('구름','6month','mix','very cute','야옹')
print(cloud.name)
print(cloud.age)
print(cloud.kind)
print(cloud.distinct)
cloud.bark()

# print(dir(Animal))