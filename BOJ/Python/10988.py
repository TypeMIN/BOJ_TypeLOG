# 소문자로 이루어진 단어 입력
Word = input()

# 앞으로 읽을 때와 거꾸로 읽을 때 똑같은지 확인
isPalindrome = Word == Word[::-1]

# 주어진 단어가 팰린드롬이라면 1 출력
if isPalindrome:
    print(1)
# 주어진 단어가 팰린드롬이 아니라면 0 출력
else:
    print(0)