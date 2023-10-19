N, M = map(int, input().split())
# -ing
# 포켓몬 이름을 저장할 리스트
poketmons = []

for _ in range(N):
    poketmon = input()
    poketmons.append(poketmon)
    
for _ in range(M):
    question = input()
    # 입력받은 문자열이 숫자로만 이루어져있으면
    if question.isdigit():
        # 인덱스로 접근하여 출력
        print(poketmons[int(question) - 1])
    else:
        # 리스트의 인덱스를 반환하여 출력
        print(poketmons.index(question)+1)