def solution(progresses, speeds):
    answer = []
    
    while progresses:
        finished = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses and progresses[0] >= 100:
            del progresses[0]
            del speeds[0]
            finished += 1
        if finished > 0:
            answer.append(finished)
            finished = 0
    return answer