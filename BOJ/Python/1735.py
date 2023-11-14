# gcd()를 사용하기 위해 import
import math

# A_1/B_1, A_2/B_2 입력
A_1, B_1 = map(int, input().split())
A_2, B_2 = map(int, input().split())

# 입력받은 두 분수의 합
A = A_1 * B_2 + A_2 * B_1
B = B_1 * B_2

# 최대공약수를 구해 분수를 기약분수로 만듦
gcd = math.gcd(A, B)
A = A // gcd
B = B // gcd

# 기약분수를 출력
print(A, B)