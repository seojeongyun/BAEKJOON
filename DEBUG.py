import sys

input = sys.stdin.readline

start, end = map(int, input().strip().split())
answer = 0
for i in range(start, end + 1):
    cnt, div = 0, 1
    while i >= div:
        if i % div == 0:
            cnt += 1
            div += 1
        else:
            div += 1
    if cnt == 3:
        answer += 1

print(answer)

