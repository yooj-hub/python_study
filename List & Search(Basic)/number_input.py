import sys
# alias
# 함수의 별칭을 주는 것으로 input이 갖고 있는 원래 값을 덮어쓴 효과를 보임
input = sys.stdin.readline

# 숫자 한개 입력 받기
n = int(input())
print(n)

# 숫자 여러개 입력 받기
# 1 2 3 이 들어올 경우
data = input().split()  # data = ['1', '2', '3']
# data에 대하여 int() 함수를 적용한 후
# map 객체를 반환
a = map(int, data)
# map 객체를 b,c,d 에 뿌려줌.
b, c, d = a
print(b, c, d)

# 위를 줄여서 다음과 같이 쓸 수 있음
x, y, z = map(int, input().split())
print(x, y, z)

# 배열에 적용해 보자.
nums = list(map(int,input().split()))
print(nums)
