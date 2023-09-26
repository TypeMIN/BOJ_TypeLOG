# N = 임씨의 옥구슬의 개수
N = int(input())

# beads = 옥구슬들의 좌표
beads = []

# 옥구슬의 좌표를 입력받아 beads에 저장
for i in range(N):
    # bead = 옥구슬의 좌표 [x, y]
    bead = list(map(int, input().split()))
    # beads에 bead 추가
    beads.append(bead)

# x_min = x좌표의 최솟값, x_max = x좌표의 최댓값
x_min = beads[0][0]
x_max = beads[0][0]
# y_min = y좌표의 최솟값, y_max = y좌표의 최댓값
y_min = beads[0][1]
y_max = beads[0][1]

# beads의 각 원소에 대해 x_min, x_max, y_min, y_max 갱신
for i in range(1, N):
    if beads[i][0] < x_min:
        x_min = beads[i][0]
    if beads[i][0] > x_max:
        x_max = beads[i][0]
    if beads[i][1] < y_min:
        y_min = beads[i][1]
    if beads[i][1] > y_max:
        y_max = beads[i][1]

# area = 옥구슬들이 이루는 직사각형의 넓이
area = (x_max - x_min) * (y_max - y_min)
print(area)