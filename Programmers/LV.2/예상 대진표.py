import math


def solution(n,a,b):
    answer = 0
    
    while True:
        # 2의 지수 토너먼트, 남은 경기수 줄여나가며 몇번째 경기에서 만나는지 판단
        # 이길때 마다 올라가면서 2씩 나눠준 것의 올림이 현재 번호
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1
        if a == b:
            break
    return answer

print("결과 = ", solution(16,2,16))
