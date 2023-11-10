def solution(word):
    answer = 0
    dic = set()
    alp = ['A', 'E', 'I', 'O', 'U', '']
    for i in range(5):
        for j in range(6):
            for k in range(6):
                for l in range(6):
                    for m in range(6):
                        dic.add(alp[i] + alp[j] + alp[k] + alp[l] + alp[m])
    l = sorted(list(dic))
    answer = l.index(word) + 1
    return answer