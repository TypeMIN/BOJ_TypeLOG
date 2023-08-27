# 정수의 개수 N
N = int(input())

# 입력된 N개의 정수
input_str = input()
# 입력된 N개의 정수를 공백을 기준으로 나누어 리스트에 저장
input_list = input_str.split()

# 찾고자 하는 정수 v
v = int(input())

# 정수 v의 개수
answer = 0

# for문을 이용하여 정수 v의 개수 구하기
for i in range(N):
  if int(input_list[i]) == v:
    answer += 1

# 정수 v의 개수 출력
print(answer)


  
  

  
  
