# 발견한 흰색 피스의 개수 입력
input_str = input()
# 띄어쓰기를 기준으로 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수를 각각 리스트에 저장
input_list = input_str.split(' ')

# 실제로 있어야하는 피스의 개수
answer_list = [1, 1, 2, 2, 2, 8]

# 실제로 있어야하는 피스의 개수가 되기위해 필요한 피스의 개수 출력
for i in range(len(input_list)):
  # 필요한 피스의 개수 = 실제로 있어야하는 피스의 개수 - 발견한 피스의 개수
  print(answer_list[i] - int(input_list[i]), end=' ')