'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120844
'''

def solution(numbers, direction):
    answer = []
    #
    if direction == 'right':
        right_val = numbers.pop()
        answer.append(right_val)
        for val in numbers:
            answer.append(val)
    else:
        answer = numbers[1:]
        answer.append(numbers[0])
    return answer

'''
    [1] 
    def solution(numbers, direction):
        return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
        
    [2]
    from collections import deque

    def solution(numbers, direction):
        numbers = deque(numbers)
        if direction == 'right':
            numbers.rotate(1)
        else:
            numbers.rotate(-1)
        return list(numbers)
'''