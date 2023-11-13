# A, B : 입력받은 두 정수
A, B = map(int, input().split())

# a, b : 유클리드 호제법을 위한 변수
a, b = A, B
while b != 0:
    # a = b * q_1 + r_1
    # b = r_1 * q_2 + r_2
    # r_1 = r_2 * q_3 + r_3
    # ...
    # r_n-2 = r_n-1 * q_n + 0
    a, b = b, a % b
# A와 B의 최대공약수는 r_n-1

# A와 B의 최소공배수는 A * B / 최대공약수
print(A * B // a)