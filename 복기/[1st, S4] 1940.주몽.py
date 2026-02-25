'''
    https://www.acmicpc.net/problem/1940

    2 / 128

    갑옷 제작
        - 제작에 사용되는 재료들은 각각 고유한 번호를 가짐
        - 갑옷은 두 개의 재료로 만듦
            - 두 재료의 번호를 합쳐 M(1 ≤ M ≤ 10,000,000)이 되면 갑옷이 만들어짐

    N개의 재료와 M이 주어졌을 때 몇 개의 갑옷을 만들 수 있는지 구하시오

    입력:
        - 첫째 줄 N(1 <= N <= 15,000)
        - 둘째 줄 M(1 <= M <= 10,000,000)
        - 셋째 줄 N 개의 번호들이 공백을 사이에 두고 ( <= 100,000)

    정렬 + 양끝
        두 수의 합, 두 수의 차
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0

    # [0] 입력
    N = int(input().strip())
    M = int(input().strip())
    data = list(map(int, input().strip().split()))

    # [1] 투포인터
    data.sort()
    start, end = 0,len(data)-1

    while True:
        current_sum = data[start] + data[end]
        if start == end:
            break

        elif current_sum >= M:
            if current_sum == M:
                answ += 1
            end -= 1

        else:
            start += 1

    print(answ)


'''
import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = 0
    v = set()

    # [0] 입력
    N = int(input().strip())
    M = int(input().strip())
    data = list(map(int, input().strip().split()))
    data.sort()

    start, end = 0, len(data)-1
    while start < end:
        if data[start] + data[end] < M:
            start += 1
        elif data[start] + data[end] > M:
            end -= 1
        else:
            answ += 1
            start += 1
            end -= 1

    print(answ)
'''
'''
TC 1
6
9
2 7 4 1 5 3
v = [0,4]

TC 2
1
2
1

TC 3
3
2
1 1 1

TC 4
5
5
1 2 5 2 3
'''

# # [1] 조합 구하기: O(N^2) -> O(15000 * 15000) -> O(15*10^3 * 15 * 10^3) -> 2.25 * 10^8  약 2억
    # # 2중 포문: 바깥 포문으로 값 하나 고정, 안쪽 포문으로 순회하면서 합이 M이 되는 경우 탐색
    # for i in range(0, N-1):
    #     for j in range(1, N):
    #         if i in v and j in v:
    #             break
    #
    #         else:
    #             if data[i]+data[j] == M:
    #                 v.add(i)
    #                 v.add(j)
    #                 answ += 1
    #                 break
    #