'''
    줄 : 1번부터 6번까지
    프렛 : 각 줄 별로 1번 부터 P번

    어떤 줄의 여러 프렛을 누르고 있다면 가장 높은 프렛의 음 발생
    EX)
        - 3번 줄의 5번 프렛을 누르고 있을 때 7번 프렛 누르면 7번 프렛의 음 발생
        - 5번 프렛은 떼지 않고 다른 손으로 7번 누르면 됨

    가장 손이 적게 움직이는 회수를 구하시오.
'''
import sys
from collections import deque

def remove_p_larger_than_me(P, answ):
    if len(melody_dict[L]) != 0:
        if melody_dict[L][-1] > P:
            for i in range(len(melody_dict[L])-1, -1, -1):
                if not melody_dict[L][i] > P:
                    break
                melody_dict[L].pop()
                answ += 1

    if len(melody_dict[L]) == 0:
        melody_dict[L].append(P)
        answ += 1

    else:
        if melody_dict[L][-1] != P:
            melody_dict[L].append(P)
            answ += 1
    return answ

if __name__ == '__main__':
    input = sys.stdin.readline
    # [0] N, P 입력
    N, _ = map(int, input().split())
    # [1] N 턴 동안 L, P 입력 받고 처리
    melody_dict = {}

    # answ = []
    #
    answ = 0
    #

    for _ in range(N):
        # [2] 해시로 처리, 줄 : key , 프렛 : value
        L, P = map(int, input().split())
        melody_dict.setdefault(L, deque())

        # 쌓여 있는 것 처리
        # while melody_dict[L]:
        #     if melody_dict[L][-1] > P:
        #         melody_dict[L].pop()
        #         answ += 1
        #     else:
        #         break

        # while melody_dict[L] and melody_dict[L][-1] > P:
        #     melody_dict[L].pop()
        #     answ += 1

        # 쌓기
        if melody_dict[L] and melody_dict[L][-1] == P:
            continue

        # melody_dict[L].append(P)
        # answ += 1

        answ = remove_p_larger_than_me(P, answ)

    print(answ)




