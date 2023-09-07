# 행렬의 크기 N, M 입력
N, M = map(int, input().split())

# 행렬 A, B 생성
A = []
B = []

# 행렬 A 입력
for i in range(N):
    # 행렬의 각 행 입력
    row = input().split()
    # 각 행의 원소를 정수로 변환
    for j in range(M):
        row[j] = int(row[j])
    # 입력받은 원소들을 행렬 A에 저장
    A.append(row)

# 행렬 B 입력
for i in range(N):
    # 행렬의 각 행 입력
    row = input().split()
    # 각 행의 원소를 정수로 변환
    for j in range(M):
        row[j] = int(row[j])
    # 입력받은 원소들을 행렬 B에 저장
    B.append(row)

# 행렬 A, B의 합 출력
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()