# 입력의 개수가 정해지지 않았기 때문에 while문 사용
while(1):
    # N = 주어진 자연수
    N = int(input())
    
    # N이 -1이면 프로그램 종료
    if N == -1:
        break
    # N이 자연수일 경우
    else:
        # divisors = N의 약수 배열
        divisors = []
        
        # N을 제외한 N의 약수 구하기
        # N을 계산하지 않기 위해 range(N - 1) 사용
        for i in range(N - 1):
            if N % (i + 1) == 0:
                divisors.append(i + 1)
        
        # N이 완전수일 경우        
        if sum(divisors) == N:
            # N = 약수1 + 약수2 + 약수3 + ... + 약수n
            # "N = ""
            print(N, '=', end=' ')
            for j in range(len(divisors)):
                if j == len(divisors) - 1:
                    # "약수n"
                    print(divisors[j])
                else:
                    # "약수i +"
                    print(divisors[j], '+', end=' ')
        # N이 완전수가 아닐 경우
        else:
            # N is NOT perfect.
            print(N, 'is NOT perfect.')