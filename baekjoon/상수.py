inputNum = input()
# " "로 스플릿해서 두개로 자르고
# 두 수 뒤집어서 비교
num0 = inputNum.split(' ')[0]
num1 = inputNum.split(' ')[1]

num0Arr = []
num1Arr = []
for i in num0:
    num0Arr.append(i)
    
for i in num1:
    num1Arr.append(i)

reverseNum0Arr = ''.join(reversed(num0Arr))
reverseNum1Arr = ''.join(reversed(num1Arr))

if reverseNum0Arr > reverseNum1Arr:
    print(reverseNum0Arr)
elif reverseNum1Arr > reverseNum0Arr:
    print(reverseNum1Arr)

