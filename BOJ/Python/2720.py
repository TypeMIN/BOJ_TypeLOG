# T = 테스트 케이스의 수
T = int(input())

# 각각의 테스트 케이스에 대해 거스름돈 계싼
for _ in range(T):
    # C = 거스름돈
    C = int(input())
    # Quarters = 쿼터(25센트)의 개수
    Quarters = C // 25
    # 쿼터로 거슬러 준 뒤 남은 거스름돈
    C %= 25
    # Dimes = 다임(10센트)의 개수
    Dimes = C // 10
    # 다임으로 거슬러 준 뒤 남은 거스름돈
    C %= 10
    # Nickels = 니켈(5센트)의 개수
    Nickels = C // 5
    # 니켈로 거슬러 준 뒤 남은 거스름돈
    C %= 5
    # Pennies = 페니(1센트)의 개수
    Pennies = C
    # 거스름돈의 개수 출력
    print(Quarters, Dimes, Nickels, Pennies)