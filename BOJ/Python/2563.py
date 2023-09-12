# N = 검은색 색종이의 수
N = int(input())

# white_paper = 100 * 100의 흰색 도화지
white_paper = [[0 for _ in range(100)] for _ in range(100)]
# black_papers = 검은색 색종이의 좌측 하단 좌표들의 배열
black_papers = []
# area = 검은색 색종이가 붙은 흰색 도화지 영역의 넓이
area = 0

# N개의 검은색 색종이의 좌측 하단 좌표들을 입력
for i in range(N):
    #i번째 검은색 색종이의 좌측 하단 좌표를 정수 배열형태로 입력 => [x, y]
    black_papers.append(list(map(int, input().split())))
    # black_papers[i][0] = i번째 검은색 색종이의 좌측 하단 좌표의 x좌표
    # black_papers[i][1] = i번째 검은색 색종이의 좌측 하단 좌표의 y좌표
    for j in range(black_papers[i][0], black_papers[i][0] + 10):
        for k in range(black_papers[i][1], black_papers[i][1] + 10):
            # 검은색 색종이로 덮인 영역 표시
            white_paper[j][k] = 1

# 검은색 색종이로 덮인 흰색 도화지의 영역 계산
for i in range(100):
    for j in range(100):
        # 1 * 1 영역의 흰색 도화지가 검은색 색종이로 덮여 있으면 white_paper[i][j] = 1
        # 따라서 배열의 모든 요소의 합 == 검은색 색종이로 덮인 흰색 도화지의 넓이
        area += white_paper[i][j]

# 검은색 색종이로 덮인 흰색 도화지의 넓이 출력    
print(area)