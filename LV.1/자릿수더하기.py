def solution(n):
    if n < 100000000:
        answer = 0
        n_list = str(n)
        for i in range(len(n_list)):
            answer += int(n_list[i])
        return answer
    else:
        answer = "N의 범위 : 100,000,000 이하의 자연수"
        return answer

# print("결과: {}".format(solution(102312312300)))
