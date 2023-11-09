def solution(n, lost, reserve):
    answer = n
    r = set(reserve) - set(lost)
    l = set(lost) - set(reserve)
    for i in l:
        if i-1 in r:
            r.remove(i-1)
        elif i+1 in r:
            r.remove(i+1)
        else:
            answer -= 1
    return answer