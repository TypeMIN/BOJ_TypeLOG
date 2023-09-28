# 삼각형들의 세 변
sides = []

# 입력의 개수가 정해져있지 않기 때문에 while문 사용
while True:
    # side = 삼각형의 세 변 = [a, b, c]
    side = list(map(int, input().split()))
    # 입력이 "0, 0, 0"이면 종료
    if side == [0, 0, 0]:
        break
    else:
        sides.append(side)

for side in sides:
    # 삼각형의 세 변을 오름차순으로 정렬
    side.sort()
    # 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 "Invalid" 출력
    if side[0] + side[1] <= side[2]:
        print("Invalid")
    # 세 변이 삼각형의 조건을 만족하는 경우
    # 세 변의 길이가 모두 같으면 "Equilateral" 출력
    # 두 변의 길이가 같으면 "Isosceles" 출력
    # 세 변의 길이가 모두 다르면 "Scalene" 출력
    else:
        if side[0] == side[1]:
            if side[1] == side[2]:
                print("Equilateral")
            else:
                print("Isosceles")
        elif side[1] == side[2]:
            print("Isosceles")
        else:
            print("Scalene")