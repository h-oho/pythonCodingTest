inputText = input()

N = int(inputText.split(' ')[0])
K = int(inputText.split(' ')[1])

coinList = []
for i in range(0, int(N)):
    inputA = input()
    coinList.append(inputA)

answer = 0
for i in range(1,len(coinList)+1):
    # 제일 큰 숫자부터 내려오면서 1 이상으로 나누어 지면
    if (K//int(coinList[0-i])) > 0:
        # 나눗셈의 몫 (코인 수)
        answer += K//int(coinList[0-i])
        # 나누고 남은 돈
        K = K%int(coinList[0-i])

print(answer)

