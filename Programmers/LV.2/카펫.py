def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            row, col = i, yellow//i
            if ((row+2)*2) + (col*2) == brown:
                return [col+2, row+2]

print("결과: {}".format(solution(8,1)))

# 약수를 구하기 위해 sqrt(yellow) 값을 해준다.
# 해당 값이 약수라면
# row 에는 약수를 col 에는 곱했을 때 yellow값이 나오는 수를 넣어준다.
# 갈색은 노란색의 테두리이기 때문에 테두리 개수를 구하는 식이 brown 개수와 같다면
# row,col에 +2 해준 후 리턴 (col >= row)