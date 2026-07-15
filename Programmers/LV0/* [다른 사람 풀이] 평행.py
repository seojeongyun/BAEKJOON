'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120875
'''

# 평행: 두 직선의 기울기가 같다
def solution(dots):
    for i in range(len(dots)):
        for j in range(len(dots)):
            if i != j and i != 3-j and j != 3-i:
                line1_delta_x = dots[i][0] - dots[j][0]
                line1_delta_y = dots[i][1] - dots[j][1]
                line2_delta_x = dots[3-i][0] - dots[3-j][0]
                line2_delta_y = dots[3-i][1] - dots[3-j][1]
                if (line1_delta_x/line1_delta_y == line2_delta_x/line2_delta_y):
                    return 1
    return 0


'''
# 입력 빠르게 받기
# 모든 경우 순회할 필요 없이 12-34 / 13-24 / 14-23 만 비교하면 됨
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0
'''