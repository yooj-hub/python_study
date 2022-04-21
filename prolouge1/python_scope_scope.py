# 전역 변수
x = 10

def func1():
    print("call by func1 :", x)

def func2():
    x = 20
    # 가까운 Scope에 있는 x = 20이 출력된다.
    print("call by func1 :", x)

def func3():
    x = 20
    def func3_2():
        # 가까운 Scope에 있는 x = 20이 출력된다.
        print("call by func3 :", x)
    func3_2()

def func4():
    x= 20
    def func4_2():
        # 가까운 Scope에 있는 x = 30이 출력된다.
        x = 30
        print("call by func4 :", x)
    func4_2()
        
# Error Case
# 두 스코프를 혼용해서 쓸 경우 Error 발생
def func5():
    print("call by func5 :", x)
    x = 30
    print("call by func5 : ", x)

func1()
func2()
func3()
func4()
func5()