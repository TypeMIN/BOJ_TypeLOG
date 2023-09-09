# 격자판 생성
A = []

# max = 최댓값
max = -1
# max_i = 최댓값의 행 번호
max_i = 0
# max_j = 최댓값의 열 번호
max_j = 0

# 9 * 9 격자판 입력
for i in range(9):
    # 입력된 문자열(행)을 int list로 변환하여 A에 추가
    A.append(list(map(int, input().split())))
    # 최댓값을 찾기 위한 반복문
    for j in range(9):
        # A[i][j]가 기존의 최댓값보다 크면 max, max_i, max_j를 갱신
        if A[i][j] > max:
            # 최댓값이 여러 개일 경우 가장 먼저 나오는 최댓값을 저장하게됨
            max = A[i][j]
            # 열과 행은 0이 아닌 1부터 시작하므로 i, j에 1을 더함
            max_i = i+1
            max_j = j+1
            
# 최댓값과 그 위치 출력
print(max)
print(max_i, max_j)