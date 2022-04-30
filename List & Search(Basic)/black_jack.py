import sys
input = sys.stdin.readline
# n, m 입력 받기
n, m = map(int, input().split())
# 두번째 줄의 숫자를 list로 입력 받기
cards = list(map(int, input().split()))

answer = -1

# 3개의 카드를 각각 골라주면된다. 카드의 순서가 상관없으므로
# 3중 반복문을 통하여 골라주면된다.
# i 번 카드 선택
for i in range(n):
    # j 번 카드 선택
    for j in range(i+1, n):
        # k 번 카드 선택
        for k in range(j+1, n):
            # 카드의 합 구하기
            tmp = cards[i] + cards[j] + cards[k]
            # m 보다 크면 안된다.
            if tmp > m:
                continue
            # 정답을 저장하지 않았거나, answer 보다 tmp가 크면 값을 바꾼다.
            if answer == -1 or tmp > answer:
                answer = tmp
# 출력
print(answer)
