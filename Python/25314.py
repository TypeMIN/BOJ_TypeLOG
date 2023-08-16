# 질문에서 주어진 N 입력
N = int(input())

# N을 4로 나눈 값만큼 "long " 출력
for _ in range(N//4):
  print("long ", end="")

# 마지막으로 "int" 출력
print("int")