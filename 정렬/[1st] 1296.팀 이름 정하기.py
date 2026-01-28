'''
    https://www.acmicpc.net/problem/1296

    2/128

    공식: ((L+O) × (L+V) × (L+E) × (O+V) × (O+E) × (V+E)) mod 100
        L: 연두의 이름과 팀 이름에서의 L 개수
        O: 연두의 이름과 팀 이름에서의 O 개수
        V: 연두의 이름과 팀 이름에서의 V 개수
        E: 연두의 이름과 팀 이름에서의 E 개수

    출력: 확률이 가장 높은 팀 이름 구하기, 팀이 여러가지인 경우 사전순으로 앞서는 팀 이름 출력

    * 1 <= L <= 20
    * N <= 50
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] 입력: O(N * L)
    NAME = input().strip()
    N = int(input().strip())
    candidate_set = set()
    for _ in range(N):
        candidate_set.add(input().strip())

    # [1] 연두 이름에서 LOVE 개수 추출
    L, O, V, E = 0, 0, 0, 0
    for char in NAME:
        if char == 'L':
            L += 1
        if char == 'O':
            O += 1
        if char == 'V':
            V += 1
        if char == 'E':
            E += 1

    # [2] 공식 계산: O(N * L)
    for candidate in candidate_set: # O(N)
        L_bk, O_bk, V_bk, E_bk = L, O, V, E
        score = 0
        for char in candidate: # O(L)
            if char == 'L':
                L_bk += 1
            if char == 'O':
                O_bk += 1
            if char == 'V':
                V_bk += 1
            if char == 'E':
                E_bk += 1
        score = ((L_bk+O_bk) * (L_bk+V_bk) * (L_bk+E_bk) * (O_bk+V_bk) * (O_bk+E_bk) * (V_bk+E_bk)) % 100
        answ.append([candidate, score])

    # [3] 정렬: O(NlogN * L)
    answ.sort(key=lambda x: (-1 * x[1], x[0]))

    # [4] 출력
    print(answ[0][0])





