# T = 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    # A, B = 두 자연수
    A, B = map(int, input().split())
    # gcb = 최대공약수
    gcb = 1
    for i in range(2, min(A, B) + 1):
        if A % i == 0 and B % i == 0:
            gcb = i
    # lcm = 최소공배수
    # 최소공배수 = 두 정수의 곱 / 최대공약수
    lcm = A * B // gcb
    # 두 자연수의 최소공배수 출력
    print(lcm)
    