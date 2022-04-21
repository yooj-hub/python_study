class Human:
    # 자신만의 원하는 data type 생성 가능
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print("hello my name is ",self.name)
        
    def inner_say_hello(self):
        print("inner ",end="")
        self.say_hello()

cs = Human("철수")
yh = Human("영희")

cs.say_hello()
yh.say_hello()
cs.inner_say_hello()
yh.inner_say_hello()
        
        
    