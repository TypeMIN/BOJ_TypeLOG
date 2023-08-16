# 영수증에 적힌 총 금액 X
X = int(input())

# 영수증에 적힌 구매한 물건의 종류의 수 N
N = int(input())

# 실제 구매한 물건의 총 금액 X_actual
X_actual = 0
# for문을 이용하여 X_actual 계산
for _ in range(N):
  # 물건의 가격과 개수 입력
  str = input()
  # 물건의 가격과 개수 분리
  str_list = str.split()
  # 물건의 실제 가격 = 물건의 가격 * 물건의 개수
  X_actual += int(str_list[0]) * int(str_list[1])
  
# 영수증에 적힌 총 금액과 실제 구매한 물건의 총 금액 비교
if X == X_actual:
  print("Yes")
else:
  print("No")