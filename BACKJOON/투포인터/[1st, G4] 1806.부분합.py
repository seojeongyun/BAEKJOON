'''
    https://www.acmicpc.net/problem/1806

    0.5 / 128

    1만 이하의 자연수로 이루어진 길이 N 수열
        - 연속된 수들의 부분합 중 그 합이 S 이상인 것 중 가장 짧은 것의 길이를 구하시오

    입력:
        - 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)
        - 둘째 줄에는 수열이 공백으로 구분되어 제공

    출력:
        - 첫째 줄에 최소 길이
        - 불가능하면 0 출력
'''
import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = sys.maxsize

    # [0] 입력
    N, M = map(int, input().strip().split())
    data = list(map(int, input().strip().split()))

    # [1] 투포인터: O(2N) = O(N) = O(10000) < 0.5초
    start, end = 0, 0
    current_sum = 0

    while True:
        if current_sum >= M:
            answ = min(answ, end-start)
            current_sum -= data[start]
            start += 1

        elif end == N:
            break

        else:
            current_sum += data[end]
            end += 1

    answ = answ if not answ == sys.maxsize else 0
    print(answ)


'''
TC 1
10 15
5 1 3 5 10 7 4 9 2 8

TC 2
10 2
1 1 1 1 1 1 1 1 1 1

TC 3
10 2
1 1 1 1 1 2 1 1 1 1

TC 4
10 14
2 2 1 1 2 2 2 2 2 5

TC 5

'''