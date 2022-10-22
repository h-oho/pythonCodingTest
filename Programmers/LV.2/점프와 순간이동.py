def solution(n):
    answer = 0
    while n != 0:
        if n%2 == 0:
            n /= 2
        else:
            n -= 1
            answer += 1
    return answer

print("결과 = ", solution(10))
