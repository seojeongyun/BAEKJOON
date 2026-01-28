'''
    포켓몬 이름이 N개 주어지고 이후 M개의 줄에 숫자 또는 포켓몬 이름이 주어진다.
        - 숫자 : 포켓몬의 이름
        - 포켓몬 이름 : 번호 출력

    출력: 이름 -> 번호 / 번호 -> 이름 출력
'''

# 양방향 접근 가능한 hash 만들 땐 dict 두 개 만들기

import sys

if __name__ == '__main__':
    # [0] 입력
    input = sys.stdin.readline
    N, M = map(int, input().rstrip().split())
    key_name_dict = {}
    key_num_dict = {}
    answ = []

    # [1] 포켓몬 도감에 기록
    for i in range(1, N+1):
        data = input().rstrip()
        key_num_dict[i] = data
        key_name_dict[data] = i

    # [2] 문제 풀이
    for _ in range(M):
        num_or_name = input().rstrip()

        # [2-2] 포켓몬 이름이 들어오면
        if num_or_name.isalpha(): # 공백 포함이면 False
            answ.append(key_name_dict[num_or_name])

        # [2-1] 번호가 들어오면    (key)
        else:
            answ.append(key_num_dict[int(num_or_name)])


    for answer in answ:
        print(answer)

