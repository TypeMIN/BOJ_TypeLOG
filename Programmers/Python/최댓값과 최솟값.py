def solution(s):
    # answer = 출력할 문자열
    answer = ''
    
    # s를 공백을 기준으로 나누어 리스트로 만들기
    s_list = s.split()
    
    # s_list의 요소들을 최댓값, 최솟값을 찾기 위해 int형으로 변환
    for i in range(len(s_list)):
        s_list[i] = int(s_list[i])
        
    # s_list의 최소값과 최대값을 문자열로 변환하여 answer에 저장
    answer = str(min(s_list)) + " " + str(max(s_list))
    
    return answer