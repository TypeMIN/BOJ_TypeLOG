# N = 주어진 자연수, K = N의 약수 중 K번째로 작은 수
N, K = map(int, input().split())

# divisor = N의 약수들
divisor = []

# N의 약수를 찾아서 divisor에 저장
for i in range(N):
    # N % (i + 1) == 0이면 i + 1은 N의 약수
    if N % (i + 1) == 0:
        divisor.append(i + 1)
 
# 약수의 수가 K보다 작으면 0 출력       
if len(divisor) < K:
    print(0)
# 약수의 수가 K보다 크거나 같으면 K번째로 작은 수 출력
else:
    print(divisor[K - 1])