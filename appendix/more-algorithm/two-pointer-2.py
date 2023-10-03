a_size = 3
b_size = 4
a = [1, 3, 5]
b = [2, 4, 6, 8]
result = [0] * (a_size + b_size)

a_idx = 0
b_idx = 0
result_idx = 0

# 아직 모든 리스트가 처리되지 않았으면 반복
while a_idx < a_size or b_idx < b_size:
    # 리스트 B가 모두 처리됐거나 리스트 A의 현재 원소가 더 작을 때 A의 현재값 채택
    if b_idx >= b_size or (a_idx < a_size and a[a_idx] <= b[b_idx]):
        result[result_idx] = a[a_idx]
        a_idx += 1
    else:
        result[result_idx] = b[b_idx]
        b_idx += 1
    result_idx += 1

print(result)  # [1, 2, 3, 4, 5, 6, 8]
