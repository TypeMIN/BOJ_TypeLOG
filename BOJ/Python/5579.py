# 제출 현황을 체크할 list 생성
assignment = [0 for _ in range(30)]

# for문을 이용하여 제출한 학생의 list 값을 1로 변경
for _ in range(28):
  # n = 제출한 학생의 번호
  n = int(input())
  # n번째 학생의 제출 현황(assignment[n-1])을 1로 변경
  assignment[n-1] = 1
  
# for문을 이용하여 제출하지 않은 학생(값이 0인 학생)의 번호 출력
for i in range(30):
  if assignment[i] == 0:
    print(i+1)