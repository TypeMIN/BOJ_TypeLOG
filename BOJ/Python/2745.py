# N = B진법 수, B = B진법
N, B = input().split()

# N을 뒤집어서 낮은 자리수부터 계산
N = N[::-1]
B = int(B)

# answer = B진법 수 N을 10진법으로 변환한 수
answer = 0

# 낮은 자리수부터 10진법으로 변환
for i in range(len(N)):
    # i번째 자리가 0 ~ 9 사이의 숫자일 경우
    if N[i].isdigit():
        # 변환한 수 = i번째 자리의 숫자 * B^i를 더함
        answer += int(N[i]) * (B ** i)
    # i번째 자리가 A ~ Z 사이의 알파벳일 경우
    else:
        # 변환한 수 = i번째 자리의 알파벳을 10진법으로 변환한 수 * B^i를 더함
        # 'A' == 65이므로 55를 빼서 10진법으로 변환
        answer += (ord(N[i]) - 55) * (B ** i)

# B진법 수 N을 10진법으로 변환한 수 출력
print(answer)