'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120860
    [1] dots의 순서가 보장되지 않음을 간과하고 두 점 사이의 거리로 풀이하려고 해서 틀림
    [2] 문제에서 '2차원 좌표 평면에 변이 축과 평행한 직사각형' 이라고 언급 -> max(x) - min(x) 가 X축의 변 길이, max(y) - min(y) 가 Y축의 변 길이
'''

def solution(dots):
    x1, x2, x3, x4 = dots[0][0], dots[1][0], dots[2][0], dots[3][0]
    y1, y2, y3, y4 = dots[0][1], dots[1][1], dots[2][1], dots[3][1]
    side_x = max([x1,x2,x3,x4]) - min([x1,x2,x3,x4])
    side_y = max([y1,y2,y3,y4]) - min([y1,y2,y3,y4])
    answer = side_x * side_y
    return answer