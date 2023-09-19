# 테스트 케이스로 "0 0"이 주어질 때 까지 반복하기 위해 while문 사용
while(1):
    # test_case = [A, B]
    test_case = list(map(int, input().split()))
    # test_case = [0, 0]이면 반복문 종료
    if test_case[0] == 0 and test_case[1] == 0:
        break
    # test_case = [A, B]일 때,
    else:
        # A가 B의 약수이면 "factor" 출력
        if test_case[1] % test_case[0] == 0:
            print("factor")
        # A가 B의 배수이면 "multiple" 출력
        elif test_case[0] % test_case[1] == 0:
            print("multiple")
        # A가 B의 약수도 배수도 아니면 "neither" 출력
        else:
            print("neither")