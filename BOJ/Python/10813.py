# N과 M을 입력
input_str = input()
input_list = input_str.split()
N = int(input_list[0])
M = int(input_list[1])

# N개의 바구니에 1부터 N까지의 공을 넣기
basket = [i+1 for i in range(N)]

# for문을 이용하여 M번의 입력을 받아 바구니에 공 바꾸기
for _ in range(M):
  # i와 j를 입력
  input_str = input()
  input_list = input_str.split()
  i = int(input_list[0])
  j = int(input_list[1])
  # i번 바구니와 j번 바구니에 들어있는 공 바꾸기
  temp = basket[i-1]
  basket[i-1] = basket[j-1]
  basket[j-1] = temp

# for문을 이용하여 바구니에 들어있는 공의 번호 출력
for i in range(N):
  print(basket[i], end=' ')