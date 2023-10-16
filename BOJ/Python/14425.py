# N과 M 입력
N, M = map(int, input().split())

# S = N개의 문자열을 담을 집합
S = set()
# N개의 문자열을 S에 입력
for _ in range(N):
    S.add(input())

# count = M개의 문자열 중 S에 있는 문자열의 개수
count = 0
# M개의 문자열을 입력받아 S에 있는지 확인
for _ in range(M):
    # S에 있으면 count 증가
    if input() in S:
        count += 1
        
# count 출력
print(count)