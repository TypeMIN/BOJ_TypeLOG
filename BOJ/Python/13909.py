import math

# N : 창문의 개수, 사람의 수
N = int(input())

# cnt : 마지막에 열여 있는 창문의 개수
cnt = 0

# 제곱수 : 약수의 개수가 홀수 개인 수
# 제곱수번째의 창문만 마지막에 열여있음
for i in range(int(math.sqrt(N))):
    # i의 제곱이 N보다 작거나 같으면 cnt를 1 증가
    if i * i <= N:
        cnt += 1

# 마지막에 열여 있는 창문의 개수 출력
print(cnt)