class Human:
    # 자신만의 원하는 data type 생성 가능
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("hello my name is ", self.name)
        
    def say_bye(self):
        print("bye bye")
# 상속할 대상을 클래스 선언 문의 ()안에 넣으면 된다.
class Student(Human):

    def __init__(self, name, school_name):
        # super 는 상위 클래스의 method를 불러올 수 있다.
        super().__init__(name)
        self.school_name = school_name

    def say_hello(self):
        super().say_hello()
        print("I'm ",self.school_name,"'s Student.", sep='')
        
cs = Student("철수", "Jeil-HighSchool")
cs.say_hello()
cs.say_bye()
