import math

# is_Prime(n) : n이 소수인지 판별하는 함수
def is_prime(n):
    # 0과 1은 소수가 아니므로 False 반환
    if n == 0 or n == 1:
        return False
    # 다른 정수로 나누어 떨어지는지 확인
    # n의 제곱근보다 더 큰 수는 확인할 필요 X
    for i in range(2, int(math.sqrt(n)) + 1):
        # 나누어 떨어지면 소수가 아니므로 False 반환
        if n % i == 0:
            return False
    # 나누어 떨어지지 않으면 소수이므로 True 반환
    return True

# T = 테스트 케이스의 개수
T = int(input())

# 테스트 케이스의 개수만큼 반복
for _ in range(T):
    # n = 입력받은 수
    n = int(input())
    # n보다 크거나 같은 가장 작은 소수를 찾을 때까지 반복
    while True:
        # n이 소수이면 n 출력 후 반복문 종료
        if is_prime(n):
            print(n)
            break
        # n이 소수가 아니면 n을 1 증가시킨 후 반복문 다시 실행
        else:
            n += 1