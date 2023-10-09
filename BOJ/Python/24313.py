# a1, a0, c, n0 입력
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# f(n) = a1 * n + a0
f_n0 = a1 * n0 + a0

# f(n)의 기울기가 c보다 클 때,
if a1 > c:
    # n이 무한히 커지면 f(n) > c * g(n)인 n가 존재
    print(0)
# f(n)의 기울기가 c와 같을 때, f(n)과 c * g(n)이 평행하므로, y절편을 비교
elif a1 == c:
    # f(n)의 y절편(a0)이 c * g(n)의 y절편(0)보다 크면
    if a0 > 0:
        # 모든 n에 대해 f(n) > c * g(n)이 성립
        print(0)
    # f(n)의 y절편(a0)이 c * g(n)의 y절편(0)보다 작거나 같으면
    else:
        # 모든 n에 대해 f(n) <= c * g(n)이 성립
        print(1)
# f(n)의 기울기가 c보다 작을 때,
else:
    # n0에서 f(n0) > c * g(n0)일 때,
    if f_n0 > c * n0:
        # n0에서 f(n) <= c * g(n)이 성립하지 않음
        print(0)
    # n0에서 f(n0) <= c * g(n0)일 때,
    else:
        # 모든 n >= n0에 대해 f(n) <= c * g(n)이 성립
        print(1)