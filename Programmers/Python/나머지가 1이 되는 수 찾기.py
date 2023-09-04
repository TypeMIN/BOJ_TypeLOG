def solution(n):
    # answer = 나머지가 1이 되는 가장 작은 자연수
    answer = 0
    
    # 1은 나머지가 1이 될 수 없으므로 2부터 시작
    for i in range(2, n):
        # n-1이 i로 나누어 떨어지면, n을 i로 나눈 나머지는 1
        if (n-1) % i == 0:
            answer = i
            # 가장 작은 자연수를 찾으면 for문 종료
            break
    
    return answer