inputText = input()

splitText = inputText.split(' ')
answer = 0
for i in splitText:
    if i != '' and i != None:
        answer += 1

print(answer)
