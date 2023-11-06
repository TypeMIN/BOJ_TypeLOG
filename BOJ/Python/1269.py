# num_A = 집합 A의 원소의 개수
# num_B = 집합 B의 원소의 개수
num_A, num_B = map(int, input().split())

# A = 집합 A 입력
A = set(map(int, input().split()))
# B = 집합 B 입력
B = set(map(int, input().split()))

# 대칭 차집합 = (A-B) & (B-A)
print(len(A-B) + len(B-A))