def solution(num):
    answer = ''
    
    # num이 짝수라면 'Even' 출력
    if num % 2 == 0:
        answer = 'Even'
    # num이 홀수라면 'Odd' 출력
    else:
        answer = 'Odd'
        
    return answer