# N과 M을 입력
input_str = input()
input_list = input_str.split()
N = int(input_list[0])
M = int(input_list[1])

# N개의 바구니 생성
basket = [0 for _ in range(N)]

# for문을 이용하여 M번의 입력을 받아 바구니에 공 넣기
for _ in range(M):
  input_str = input()
  input_list = input_str.split()
  # i = 넣기 시작할 바구니
  i = int(input_list[0])
  # j = 마지막으로 넣을 바구니
  j = int(input_list[1])
  # k = 넣을 공의 번호
  k = int(input_list[2])
  # i-1번째 바구니(i번 바구니)부터 j-1번째 바구니(j번 바구니)까지 k번 공을 넣기
  for i in range(i-1, j):
    basket[i] = k

# for문을 이용하여 바구니에 들어있는 공의 번호 출력
for i in range(N):
  print(basket[i], end=' ')