
def fibo(n):
    # 종료 조건
    if n <= 2:
        return 1
    # 해당 수열의 조건
    return fibo(n-1) + fibo(n-2)


print(fibo(10))
