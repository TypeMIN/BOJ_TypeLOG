def solution(citations):
    answer = 0
    
    citations.sort()
    for h in range(len(citations) + 1):
        for j in range(len(citations)):
            if citations[j] >= h:
                if len(citations) - j >= h:
                    answer = h
    
    return answer