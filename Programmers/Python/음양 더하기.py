def solution(absolutes, signs):
    # answer = 정수들의 합
    answer = 0
    
    for i in range(len(signs)):
        # signs[i]가 True이면, absolutes[i]는 양수
        if signs[i]:
            answer += absolutes[i]
        # signs[i]가 False이면, absolutes[i]는 음수
        else:
            answer -= absolutes[i]
            
    return answer