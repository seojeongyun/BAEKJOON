'''
    https://www.acmicpc.net/problem/13305

    2 / 512

    N개의 도시
        - 인접한 도시 사이의 도로는 서로 길이가 다를 수 있다.

    차를 타고 제일 왼쪽 도시에서 오른쪽 도시로 이동
        - 처음 출발 시 기름이 없어서 기름을 넣어야 함.
        - 기름통의 크기는 무제한
        - 1km마다 1L 사용
        - 각 도시에는 단 하나의 주유소가 존재하며, 가격은 도시마다 다름
        - 원 안의 숫자는 도시의 주유소 리터당 가격

    제일 왼쪽 도시에서 오른쪽 도시로 이동하는 최소의 비용을 계산

    입력:
        - 첫 번째 줄에는 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000)
        - 다음 줄에는 인접한 두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터 N-1개의 자연수로 주어진다.
        - 다음 줄에는 주유소의 리터당 가격이 제일 왼쪽 도시부터 순서대로 N개의 자연수로 주어진다.
        - 제일 왼쪽 도시부터 제일 오른쪽 도시까지의 거리는 1이상 1,000,000,000 이하의 자연수이다.
        - 리터당 가격은 1 이상 1,000,000,000 이하의 자연수이다.

    출력:
        제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력한다.
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    # [0] 입력
    N = int(input().strip())
    dist = list(map(int, input().strip().split()))
    cost = list(map(int, input().strip().split()))

    # [1] 그리디
    min_cost = cost[0]
    total_cost = 0

    for i in range(N-1):
        if min_cost > cost[i]:
            min_cost = cost[i]
        total_cost += min_cost*dist[i]

    print(total_cost)