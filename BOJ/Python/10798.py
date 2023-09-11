# word = 주어진 5개의 단어
words = []

# 주어진 단어를 입력
for _ in range(5):
    words.append(input())

# j번째 글자를 출력
for j in range(15):
    # i번째 단어를 출력
    for i in range(5):
        # i번째 단어의 j번째 글자가 존재하면 출력
        if len(words[i]) > j:
            print(words[i][j], end='')