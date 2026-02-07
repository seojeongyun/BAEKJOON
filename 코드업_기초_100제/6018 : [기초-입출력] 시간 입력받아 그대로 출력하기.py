'''
24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.
'''

splited_input = input().split(':')
hour, min = splited_input[0], splited_input[-1]
print(hour + ':' + min)