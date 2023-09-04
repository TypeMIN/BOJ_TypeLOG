def solution(sides):
    answer = 0
    # 가장 긴 변이 나머지 두 변의 합보다 작은 경우 == 세 변의 합이 가장 긴 변의 두배보다 큰 경우
    if sum(sides) - 2 * max(sides) > 0:
        answer = 1
    # 가장 긴 변이 나머지 두 변의 합보다 크거나 같은 경우 == 세 변의 합이 가장 긴 변의 두배보다 작거나 같은 경우
    else:
        answer = 2 
    return answer