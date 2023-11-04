# N = 듣도 보도 못한 사람의 수
# M = 보도 못한 사람의 수 입력
N, M = map(int, input().split())

# N_list = 듣도 못한 사람의 리스트
N_list = []
# M_list = 보도 못한 사람의 리스트
M_list = []

# 듣도 못한 사람의 리스트 입력
for _ in range(N):
    N_list.append(input())
# 보도 못한 사람의 리스트 입력
for _ in range(M):
    M_list.append(input())

# 듣도 보도 못한 사람의 리스트 = 듣도 못한 사람 AND 보도 못한 사람
# 사전순으로 정렬
result = sorted(list(set(N_list) & set(M_list)))

# 듣도 보도 못한 사람의 수 출력
print(len(result))
# 듣도 보도 못한 사람의 이름 출력
for i in result:
    print(i)
