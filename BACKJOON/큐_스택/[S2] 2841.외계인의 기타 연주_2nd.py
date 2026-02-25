'''
    기타
    - 1번부터 6번 줄 존재
        - 각 줄은 1번부터 P번까지의 프렛으로 나뉨

    멜로디
    - 줄에서 해당하는 프렛을 누르고 팅기면 연주
        - 어떤 줄의 프렛을 여러개 누르고 있다면 가장 높은 프렛의 음 발생
            - 3번 줄의 5번 프렛을 이미 누르고 있는 상태에서 7번 프렛 음을 내고 싶으면
            5번 안 떼고 7번만 누르면 됨

    출력: 어떤 멜로디가 주어졌을 때, 손가락이 가장 적게 움직이는 회수를 구하시오.
'''

import sys

def count(fret_lst):
    cnt = 0
    pressed_frets = []

    # [0] lst에서 fret 값 하나 pop, 현재 누르고 있는 프렛 리스트 관리
    for fret in fret_lst:
        # [1] 아무것도 안 눌려 있는 경우
        if len(pressed_frets) == 0:
            cnt += 1
            pressed_frets.append(fret)

        # [2] 이미 눌려있는 경우 크기 비교
        else:
            # [2-1] 누르고 있는 프렛보다 큰 프렛 누르면
            if max(pressed_frets) < fret:
                pressed_frets.append(fret)
                cnt += 1

            # [2-2] 누르고 있는 프렛보다 작은 거 누르면
            elif max(pressed_frets) > fret:
                for i in range(len(pressed_frets)-1, -1, -1):
                    if pressed_frets[i] > fret:
                        pressed_frets.pop()
                        cnt += 1
                    else:
                        break
                if len(pressed_frets) == 0 or pressed_frets[-1] < fret:
                    pressed_frets.append(fret)
                    cnt += 1

    return cnt

if __name__ == '__main__':
    input = sys.stdin.readline
    answer = 0
    # [0] 입력 및 데이터 생성
    N, P = map(int, input().rstrip().split())

    # melody = {2: [], 3: [], ..}, 순서가 저장된 딕셔너리
    melody = {}
    for _ in range(N):
        line, fret = map(int, input().rstrip().split())
        melody.setdefault(line, [])
        melody[line].append(fret)

    # [1] 줄 별로 손가락 움직이는 회수 카운트
    for k in melody.keys():
        cnt = count(melody[k])
        answer += cnt

    print(answer)