# 주어진 문자열 입력
s = input()

# 세 개의 정수를 공백을 기준으로 구분하여 리스트에 저장
s_list = s.split()

# for문을 이용하여 세 정수의 합 계산
sum = 0
for i in s_list:
    sum += int(i)

# A+B+C의 값 출력
print(sum)