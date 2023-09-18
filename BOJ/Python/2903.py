# N = 지형을 만드는 과정의 횟수
N = int(input())

# 만들어진 지형의 가로 크기
num_rows = 2 ** N + 1
# 만들어진 지형의 세로 크기
num_columns = 2 ** N + 1

# 중복되는 점은 한 번만 고려한 점의 수
num_points = num_rows * num_columns

# 점의 수 출력
print(num_points)