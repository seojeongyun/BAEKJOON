'''
    https://www.acmicpc.net/problem/2559

    1 / 128

    연속적인 ?일 간의 온도의 합이 가장 큰 값을 계산

    입력:
        N, K: 날짜의 수 (2 <= N <= 10만), 연속 날짜 수 (1 <= K <= N)
        온도

    출력:
        최대 값
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = -sys.maxsize

    # [0] 입력
    N, K = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))

    # [1] 투포인터
    start, end, current_sum = 0, 0, 0

    while True:
        if end - start == K:
            answ = max(answ, current_sum)
            if end < len(data):
                current_sum += data[end]
                current_sum -= data[start]
                start += 1
                end += 1
            else:
                break

        else:
            current_sum += data[end]
            end += 1

    print(answ)

'''
TC1 
10 2
3 -2 -4 -9 0 3 7 13 8 -3

TC2
10 5
3 -2 -4 -9 0 3 7 13 8 -3

TC3 
9 2
-1 -2 3 4 12 0 0 -1 26

TC4
5 4
-1 -1 -1 -1 -1

TC5
5 5
-1 -1 -1 -1 -1
'''