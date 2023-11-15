# gcd()를 사용하기 위해 import
import math

# N : 이미 심어져 있는 나무의 수
N = int(input())

# trees : 이미 심어져 있는 나무의 위치
trees = []
# gcd : 첫 번째 나무를 기준으로 한 각 나무 거리의 최대공약수
gcd = 0

for i in range(N):
    # 첫 번째 나무의 위치를 저장
    if i == 0:
        trees.append(int(input()))
    # 두 번째 나무부터는 첫 번째 나무를 기준으로 위치를 저장
    else:
        # 첫 번째 나무를 기준으로 한 i번째 나무의 위치 = 기준점과의 거리 - 첫 번째 나무의 위치
        tree = int(input()) - trees[0]
        # 두 번째 나무일 경우
        if i == 1:
            # 최대공약수를 구하기 위해 위치 저장
            gcd = tree
        else:
            # 최대공약수 구하기
            gcd = math.gcd(gcd, tree)
        # 나무 위치 저장
        trees.append(tree)
        
# 모두 같은 간격이기 위한 모든 나무의 수 = 마지막 나무의 위치 // 최대공약수
# 필요한 나무의 수 = 모두 같은 간격이기 위한 모든 나무의 수 - 이미 심어져 있는 나무의 수
print((trees[-1] // gcd) - (N - 1))
    
