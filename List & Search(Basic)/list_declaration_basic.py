# problem 1
# 방법 1 (직접 설정)
sol1_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 방법 2 (for, while Loop 를 사용한다.)
# 빈 리스트를 생성한다.
sol1_2 = []
for i in range(1, 6):
    sol1_2.append(i)
j = 6
while(j <= 10):
    sol1_2.append(j)
    j += 1

# 방법 3 range 이용
sol1_3 = list(range(1, 11))

# 방법 4 list comprehension
sol1_4 = [i for i in range(1, 11)]

# problem 2
# for/while loop와 직접 선언하는 것은 생략
sol2_1 = list(range(21,31,2))
sol2_2 = [i for i in range(20, 31) if i % 2 ==1]

# problem 3

sol3_1 = [[[0] * 10]* 4] * 5
sol3_2 = [[[0] * 10 for _ in range(4)]for _ in range(5)]

# problem 4

sol4 = [[[] for _ in range(3)] for _ in range(3)]


