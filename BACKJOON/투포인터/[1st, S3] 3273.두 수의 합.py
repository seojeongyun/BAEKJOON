'''
    https://www.acmicpc.net/problem/3273

    1 / 128

    n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열
        ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수

    자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램

    입력:
        첫째 줄에 수열의 크기 n
        다음 줄에는 수열에 포함되는 수
        셋째 줄에는 x가 주어진다.
        (1 ≤ n ≤ 100000, 1 ≤ x ≤ 2000000)

    출력:
        조건을 만족하는 쌍의 개수
'''
import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N = int(input().strip())
    data = list(map(int, input().strip().split()))
    M = int(input().strip())

    # [1] 투포인터
    data.sort()
    start, end = 0, len(data)-1

    while True:
        if start == end:
            break

        if data[start] + data[end] == M:
            answ += 1
            end -= 1

        else:
            if data[start] + data[end] < M:
                start += 1
            else:
                end -= 1

    print(answ)