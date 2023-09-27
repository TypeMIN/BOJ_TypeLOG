# 삼각형의 세 각
angles = []

# 삼각형의 세 각을 입력
for _ in range(3):
    angles.append(int(input()))
# 각을 오름차순으로 정렬
angles.sort()

# 각의 합이 180이 아니면 Error 출력
if sum(angles) != 180:
    print("Error")
# 각의 합이 180이고,
# 세 각의 크기가 모두 60이면 Equilateral 출력
# 두 각의 크기가 같으면 Isosceles 출력
# 세 각의 크기가 모두 다르면 Scalene 출력
else:
    if angles[0] == angles[1]:
        if angles[1] == angles[2]:
            print("Equilateral")
        else:
            print("Isosceles")
    elif angles[1] == angles[2]:
        print("Isosceles")
    else:
        print("Scalene")