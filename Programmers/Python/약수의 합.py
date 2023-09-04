def solution(n):
    # answer = 약수의 합
    answer = 0
    
    # for문을 이용하여 n의 약수 찾기
    for i in range(n):
        # n을 (i+1)로 나누었을 때 나머지가 0이면 (i+1)은 n의 약수
        if n % (i+1) == 0:
            answer += (i+1)
    
    return answer