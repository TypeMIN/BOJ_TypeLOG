def solution(clothes):
    answer = 1
    dic = {}
    for item, genre in clothes:
        if genre not in dic:
            dic[genre] = 1
        else:
            dic[genre] += 1
    for genre in dic:
        answer *= dic[genre] + 1
    answer -= 1
    return answer