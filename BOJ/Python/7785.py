# n = 로그에 기록된 출입 기록의 수
n = int(input())

# log = 현재 회사에 있는 사람
log = set()

# n개의 출입 기록을 확인
for _ in range(n):
    # name = 이름, status = [enter, leave]
    name, status = input().split()
    # status가 enter이면 log에 name을 추가 (출근)
    if status == 'enter':
        log.add(name)
    # status가 leave이면 log에서 name을 제거 (퇴근)
    else:
        log.remove(name)

# log를 사전 순의 역순으로 정렬
log = sorted(log, reverse=True)

# log에 있는 이름을 출력
for name in log:
    print(name)