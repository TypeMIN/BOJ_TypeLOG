# 입력의 개수를 알 수 없기 때문에 while문을 사용하여 EOF까지 입력
while True:
  # try-except문을 사용하여 EOF에 도달하면 break
  try:
    # input()으로 입력받은 문자열을 그대로 출력
    print(input())
  except EOFError:
    # EOF에 도달하면 프로그램 종료
    break