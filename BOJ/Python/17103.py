# T : 테스트 케이스의 개수
T = int(input())

# prime[i] : i가 소수이면 True, 아니면 False
prime = [True] * 1000001
# 0과 1은 소수가 아니므로 False로 설정
prime[0] = prime[1] = False
# 에라토스테네스의 체를 이용하여 소수 판별
for i in range(2, 1000001):
    if prime[i]:
        for j in range(i * i, 1000001, i):
            prime[j] = False

for _ in range(T):
    # N : 입력받은 수
    N = int(input())
    # cnt : N의 골드바흐 파티션의 개수
    cnt = 0
    # i와 N - i가 모두 소수이면 cnt를 1 증가
    for i in range(2, N // 2 + 1):
        if prime[i] and prime[N - i]:
            cnt += 1        
    # N의 골드바흐 파티션의 개수 출력
    print(cnt)