def solution(n):
    # answer = 각 자릿수의 합
    answer = 0

    # 각 자릿수로 분리하기 위해 문자열로 변환
    n_str = str(n)
    # for문을 이용하여 각 자릿수의 합 구하기
    for i in range(len(n_str)):
        answer += int(n_str[i])

    return answer