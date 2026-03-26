'''
    조규현 좌표: x1, y1
    백승환 좌표: x2, y2
    조규현-마린 거리: r1
    백승환-마린 거리: r2

    가 주어졌을 때 마린이 있을 수 있는 좌표의 수 출력

    마린이 있을 수 있는 좌표의 수가 무한대면 -1 출력
'''

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    answ_lst = []
    T = int(input().strip())

    for _ in range(T):
        x1,y1,r1,x2,y2,r2 = map(int, input().strip().split())
        dist = ((x1-x2)**2 + (y1-y2)**2) ** (1/2)

        # 같은 중심점일 때
        if x1 == x2 and y1 == y2:
            if r1 == r2: answ_lst.append(-1)
            else: answ_lst.append(0)

        # 다른 중심점일 때
        else:
            # 내접 ~ 외접
            if abs(r1-r2) < dist < abs(r1+r2):
                answ_lst.append(2)
            # 외접
            elif abs(r1+r2) == dist:
                answ_lst.append(1)
            # 내접
            elif abs(r1-r2) == dist:
                answ_lst.append(1)
            # 그 외=겹치지 않을 때
            else:
                answ_lst.append(0)

    for answ in answ_lst:
        print(answ)
'''
TC1
1
0 0 1 0 0 1


1
1 2 5 2 2 4

1
0 0 22 0 0 2
'''



