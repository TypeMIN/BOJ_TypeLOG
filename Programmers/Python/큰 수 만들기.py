def solution(number, k):
    answer = ''
    stack = []
    
    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1      
        stack.append(i)
    if k > 0:
        for _ in range(k):
            stack.pop()
    for i in stack:
        answer += i
    return answer