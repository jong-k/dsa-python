data_size = 5
data = [10, 20, 30, 40, 50]

# prefix sum 배열 만들기
prefix_sum = [0]
sum_val = 0
for num in data:
    sum_val += num
    prefix_sum.append(sum_val)

# 구간 합 계산
left = 3
right = 5
print(prefix_sum[right] - prefix_sum[left - 1])  # 120
