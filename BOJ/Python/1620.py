import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 포켓몬을 저장할 딕셔너리
poketmons = dict()

for i in range(N):
    poketmon = input().rstrip()
    # {번호 : 이름}, {이름 : 번호} 형태로 저장
    poketmons[i + 1] = poketmon
    poketmons[poketmon] = i + 1
    
for _ in range(M):
    question = input().rstrip()
    # 입력받은 문자열이 숫자로만 이루어져있으면
    if question.isdigit():
        # 번호를 통해 포켓몬의 이름을 출력
        print(poketmons[int(question)])
    else:
        # 이름을 통해 포켓몬의 번호를 출력
        print(poketmons[question])