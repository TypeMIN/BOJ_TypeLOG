import sys
input = sys.stdin.readline

# N = 상근이가 가지고 있는 숫자 카드의 개수
N = int(input())

# cards = 상근이가 가지고 있는 숫자 카드
cards = set(map(int, input().split()))

# M = 비교할 정수의 개수
M = int(input())

# nums = 비교할 정수
nums = list(map(int, input().split()))

# 모든 비교할 정수에 대해
for num in nums:
    # 해당 정수가 적힌 숫자 카드를 상근이가 가지고 있다면 1, 아니면 0을 출력
    if num in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')