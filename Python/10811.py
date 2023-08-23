# N과 M을 입력
input_str = input()
input_list = input_str.split()
N = int(input_list[0])
M = int(input_list[1])

# N개의 바구니 생성
basket = [i+1 for i in range(N)]

# for문을 이용하여 M번의 입력을 받아 바구니의 순서 바꾸기
for _ in range(M):
  input_str = input()
  input_list = input_str.split()
  # i = 바구니의 순서를 바꾸기 시작할 위치
  i = int(input_list[0])
  # j = 바구니의 순서를 바꾸기 마지막 위치
  j = int(input_list[1])
  # i번째 바구니(basket[i-1])부터 j번째 바구니(basket[j-1])까지의 순서를 바꾸기
  basket[i-1:j] = basket[i-1:j][::-1]

# for문을 이용하여 가장 왼쪽에 있는 바구니부터 출력 
for i in range(N):
  print(basket[i], end=' ')