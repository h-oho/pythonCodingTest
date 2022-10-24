def solution(n):
    answer = 0
    # *2 할때는 비용이 들지 않으므로 짝수이동시 pass (+0)
    while n != 0:
        if n%2 == 0:
            n /= 2
        else:
            # 한칸(홀수)이동 시에 +1
            n -= 1
            answer += 1
    return answer

print("결과 = ", solution(1000))
