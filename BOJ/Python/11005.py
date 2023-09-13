# N = 입력된 10진수 수, ㅠ = B진법
N, B = map(int, input().split())

# answer = B진법으로 변환된 N의 값
answer = ""

# 10진법 수 N을 B진법으로 변환
while N > 0:
    # B진법의 자리 수 = N을 B로 나눈 나머지
    digit = N % B
    # 새로운 N = N을 B로 나눈 몫
    N = N // B
    # 입력할 수가 10 이상이면 알파벳으로 변환
    if digit >= 10:
        # e.g. 'A' = 65 = 10 + 55
        answer += chr(digit + 55)
    # 입력할 수가 10 미만이면 그대로 입력
    else:
        answer += str(digit)

# B진법으로 변환된 N의 값은 거꾸로 입력되어있으므로 반대로 출력
answer = answer[::-1]
print(answer)