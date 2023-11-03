N, M = map(int, input().split())

N_list = []
M_list = []

for _ in range(N):
    N_list.append(input())
    
for _ in range(M):
    M_list.append(input())
    
result = sorted(list(set(N_list) & set(M_list)))

print(len(result))
for i in result:
    print(i)
