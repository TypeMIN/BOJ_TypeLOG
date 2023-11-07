# S = 입력받은 문자열
S = input()

# sub_S = S의 부분 문자열 집합
sub_S = set()

# S의 부분 문자열을 sub_S에 추가
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        sub_S.add(S[i:j])

# sub_S의 원소의 개수 출력        
print(len(sub_S))