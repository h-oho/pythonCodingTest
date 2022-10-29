inputNumber = int(input())
for i in range(0, inputNumber):
    inputText = input()
    # 연속적인 char인지 AND 이전에 나왔던 char인지
    # 앞 or 뒤가 같은게 있는지 있으면 PASS
    # 이전 char들을 탐색해서 없으면 PASS
    # 둘 다 만족하지 않으면 전체 갯수에서 -1
    
    for j in range(len(inputText)-1):
        # 앞단어와 뒷 단어가 같은지 다른지 판단
        if inputText[j] != inputText[j+1]:
            # 다른 경우 그 뒤에 같은 단어가 또 나오는지 체크
            if inputText[j] in inputText[j+1:]:
                # 또 나온다면 그룹단어가 아니므로 -1 시키고 break
                inputNumber -= 1
                break
print(inputNumber)