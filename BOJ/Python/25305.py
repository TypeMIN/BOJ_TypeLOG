# N = 응시자의 수, k = 상을 받는 사람 수
N, k = map(int, input().split())

# scores = 각 학생들의 점수를 저장하는 배열
scores = list(map(int, input().split()))

# scores를 내림차순으로 정렬
scores.sort(reverse=True)

# k번째로 높은 점수(커트라인)를 출력
print(scores[k-1])