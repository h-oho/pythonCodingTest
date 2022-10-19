def solution(n):
    answer = ''
    if n%2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

# print("결과: {}".format(solution(12)))