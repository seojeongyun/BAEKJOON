'''
    https://www.acmicpc.net/problem/2816

    1 / 128

    채널 리스트
        모든 채널의 이름은 서로 다르고 항상 KBS1과 KBS2를 포함

    채널 리스트를 조절해 KBS1을 첫 번째로, KBS2를 두 번째로 만들려고 한다.
        1. 화살표를 한 칸 아래로 내린다. (채널 i에서 i+1로)
        2. 화살표를 위로 한 칸 올린다. (채널 i에서 i-1로)
        3. 현재 선택한 채널을 한 칸 아래로 (채널 i와 i+1의 위치 스왑, 화살표는 i+1을 가리키고 있는다)
        4. 현재 선택한 채널을 위로 한 칸 (채널 i와 i-1의 위치 스왑, 화살표는 i-1을 가리키고 있는다)
        * 화살표가 채널 리스트의 범위를 넘으면 명령 무시

    입력:
        - 채널 수 N
        - N개 줄에 채널 이름이 한 줄에 하나 씩

    출력:
        - 눌러야 하는 버튼을 순서대로 공백 없이 출력
'''

import sys
from collections import deque

def search_kbs(ptr, channel):
    while True:
        if channels[ptr] == channel:
            break

        ptr += 1
        answ.append('1')

    return ptr

if __name__ == '__main__':
    input = sys.stdin.readline
    answ = []

    # [0] 입력
    N = int(input().strip())
    channels = deque(input().strip() for _ in range(N))

    ptr = 0
    tmp_channel = 0

    # [1] KBS1 찾으러 내려가기
    ptr = search_kbs(ptr, channel='KBS1')

    # [2] KBS1 제일 위로올리고 ptr 초기화
    del channels[ptr]
    channels.appendleft('KBS1')
    for _ in range(ptr):
        answ.append('4')

    ptr = 0

    # [3] KBS2 찾으러 내려가기
    ptr = search_kbs(ptr, channel='KBS2')

    # [4] KBS2 위에서 두 번째로 올리기
    for _ in range(ptr-1):
        answ.append('4')

    print(''.join(answ))





