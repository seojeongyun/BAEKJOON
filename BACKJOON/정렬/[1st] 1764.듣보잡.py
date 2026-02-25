'''
    https://www.acmicpc.net/problem/1764

    2 / 256

    듣지도 못한 사람의 명단과
    보지도 못한 사람의 명단

    출력: 듣도 보도 못한 사람의 명단을 사전순으로

    입력:
        듣도 못한 사람의 수 N
        보도 못한 사람의 수 M
        N개의 줄에 걸쳐 듣도 못한 사람의 이름,
        다음 줄 부터 보도 못한 사람의 이름이 순서대로
'''

import sys
from collections import defaultdict

if __name__ == '__main__':
    input = sys.stdin.readline
    name_counter = defaultdict(int)
    answ = []

    # [0] 입력
    N, M = map(int, input().strip().split())
    name_lst = [input().strip() for _ in range(N+M)]

    for name in name_lst:
        name_counter[name] += 1

    # [1] 중복 처리: 듣도 보도 못한 사람 추출
    for key in name_counter.keys():
        if name_counter[key] >= 2:
            answ.append(key)

    answ.sort(key=lambda x: x)

    print(len(answ))
    for name in answ:
        print(name)

