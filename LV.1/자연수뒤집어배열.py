def solution(n):
    answer = []
    reverseAnswer = reversed(str(n))
    for i in reverseAnswer:
        answer.append(int(i))
    return answer

# print("결과: {}".format(solution(141512)))