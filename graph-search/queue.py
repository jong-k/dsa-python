from collections import deque

queue = deque()  # []

queue.append(1)  # [ 1 ]
queue.appendleft(2)  # [ 2, 1 ]
queue.appendleft(3)  # [ 3, 2, 1 ]
queue.popleft()  # [ 2, 1 ]
queue.pop()  # [ 2 ]

print(queue)  # deque([2])
# queue를 list로 바꾸기
queue = list(queue)
print(queue)  # [2]
