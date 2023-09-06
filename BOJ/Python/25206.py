# credits = 치훈이가 들은 학점의 합
credits = 0.0
# grades = 치훈이가 들은 (학점 * 과목평점)의 합
grades = 0.0

# 20개의 과목 입력
for i in range(20):
    course = input()
    # course = 과목명, credit = 학점, grade = 과목평점
    course, credit, grade = course.split()
    # 과목평점에 따라  credits와 grades 계산
    if grade == 'A+':
        credits += float(credit)
        grades += float(credit) * 4.5
    elif grade == 'A0':
        credits += float(credit)
        grades += float(credit) * 4.0
    elif grade == 'B+':
        credits += float(credit)
        grades += float(credit) * 3.5
    elif grade == 'B0':
        credits += float(credit)
        grades += float(credit) * 3.0
    elif grade == 'C+':
        credits += float(credit)
        grades += float(credit) * 2.5
    elif grade == 'C0':
        credits += float(credit)
        grades += float(credit) * 2.0
    elif grade == 'D+':
        credits += float(credit)
        grades += float(credit) * 1.5
    elif grade == 'D0':
        credits += float(credit)
        grades += float(credit) * 1.0
    elif grade == 'F':
        credits += float(credit)
        grades += float(credit) * 0.0
    # 과목평점이 P일 경우 계산하지 않음
    else:
        pass

# 전공평점 = (학점 * 과목평점)의 합 / 학점의 합
average = grades / credits
print(average)