# nums = 5개의 정수
nums = []

# 5개의 정수를 입력받아 nums에 저장
for _ in range(5):
    nums.append(int(input()))

# nums에 저장된 5개의 정수를 오름차순으로 정렬
nums.sort()

# avg = 5개 정수의 평균 = 5개 정수의 합 / 5
avg = sum(nums) // 5
# mid = 5개 정수의 중앙값 = 3번째로 작은 정수
mid = nums[2]

print(avg)
print(mid)