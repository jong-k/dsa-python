data_size = 5
target_sum = 5
data = [1, 2, 3, 2, 5]
count = 0
interval_sum = 0  # 부분합
end = 0

# start를 1씩 증가시키며 반복
for start in range(data_size):
    # end를 가능한 만큼 이동시키기
    while interval_sum < target_sum and end < data_size:
        interval_sum += data[end]
        end += 1
    # 부분합 = target 이면 카운트하고 start +1 해주기
    if interval_sum == target_sum:
        count += 1
    interval_sum -= data[start]

print(count)  # 3
