# sides = 세 막대의 길이 = [a, b, c]
sides = list(map(int, input().split()))

# 세 막대의 길이를 오름차순으로 정렬
sides.sort()

# 세 막대로 삼각형을 만들 수 있는 경우
if sides[0] + sides[1] > sides[2]:
    # 세 막대의 길이의 합 = 세 막대로 만들 수 있는 가장 큰 삼각형의 둘레
    print(sum(sides))
# 세 막대로 삼각형을 만들 수 없는 경우
else:
    # 가장 긴 막대의 길이 = 다른 두 막대의 길이의 합 - 1
    sides[2] = sides[0] + sides[1] - 1
    print(sum(sides))