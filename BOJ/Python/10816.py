import sys
input = sys.stdin.readline

# N = 상근이가 가지고 있는 숫자 카드의 개수
N = int(input())

# cards = 상근이가 가지고 있는 숫자 카드
cards = [0 for _ in range(20000001)]

# cards[card] = 상근이가 가지고 있는 card의 개수
for card in map(int, input().split()):
    cards[card + 10000000] += 1

# M = 비교할 정수의 개수
M = int(input())

# nums = 비교할 정수
nums = list(map(int, input().split()))

# 모든 비교할 정수에 대해
for num in nums:
    # 상근이가 가지고 있는 숫자 카드의 개수를 출력
    print(cards[num + 10000000], end=' ')