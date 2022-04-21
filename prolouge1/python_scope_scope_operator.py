# 전역 변수 
x = 10

def func1():
    # 전역 변수에 있는 x를 명시
    global x
    print("call by func1 :", x)

def func2():
    x = 20
    def func2_2():
        # 내부 함수 또한 global 일 경우 전역 변수 호출
        global x
        print("call by func2 :", x)
    func2_2()
# nonlocal 은 자신을 감싼 함수의 변수를 가져온다.
def func3():
    x = 20
    def func3_2():
        nonlocal x
        print("call by func3 :", x)
    func3_2()

# global scope operator나 nonlocal scope operator로
# 변수를 불러올 경우 변경이 가능하다.
def func4():
    global x

    x = 40
    print("call by func4 :", x)

def func5():
    x = 30
    def func5_2():
        nonlocal x
        x = 20
    func5_2()
    print("call by func5 :", x)
    
    
    
        

func1()
func2()
func3()
print("전역변수 x 값 변경")
func4()
func1()
func5()
