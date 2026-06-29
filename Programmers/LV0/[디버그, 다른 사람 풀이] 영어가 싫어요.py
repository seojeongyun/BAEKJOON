'''
    https://school.programmers.co.kr/learn/courses/30/lessons/120894
    [1] replace: numbers.replace(k, r[k])면 numbers에서 k를 r[k]로 대체
'''


def solution(numbers):
    dict_ = {"zero": '0',
             "one": '1',
             "two": '2',
             "three": '3',
             "four": '4',
             "five": '5',
             "six": '6',
             "seven": '7',
             "eight": '8',
             "nine": '9'}
    start = 0
    answer = ''
    for i in range(len(numbers)+1):
        if numbers[start:i] in dict_.keys():
            answer += dict_[numbers[start:i]]
            start = i
    return answer

solution("onetwothreefourfivesixseveneightnine")

'''
    def solution(numbers):
        r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
             'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        for k in r.keys():
            numbers = numbers.replace(k, r[k])
    
        return int(numbers)
'''