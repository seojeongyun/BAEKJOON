'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120863#
'''

def solution(polynomial):
    # 양의 정수, 공백, 'x', '+'
    # 결과에 상수항은 마지막
    v_num = 0
    c_num = 0
    for char in polynomial.split():
        if 'x' in char:
            if char == 'x':
                v_num += 1
            else:
                v_num += int(char[:-1])
        elif char.isdigit():
            c_num += int(char)

    if v_num != 0 and c_num == 0:
        answer = str(v_num)+'x' if v_num != 1 else 'x'
    elif v_num == 0 and c_num != 0:
        answer = str(c_num)
    else:
        answer = str(v_num)+'x + '+str(c_num) if v_num != 1 else 'x + '+str(c_num)
    return answer