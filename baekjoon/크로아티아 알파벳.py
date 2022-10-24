input = input()
answer = 0
cList = ['c=','c-','dz=','d-','lj','nj','s=','z=']
temp = ''

# 입력 받은 문자열 for 문으로 돌려서 한 글자씩 temp에 넣어주면서 글자수 +1
for i in input:
    temp += i
    answer += 1
    for j in cList:
        # 한글자씩 들어간 temp에 cList에 있는 것들이 있는지 확인
        Yn = temp.find(j)
        if Yn >= 0:
            # c-와 같이 2글자면 +2가 됐지만 한 문자로 쓰여야 하기 때문에 -1 시켜줌
            # 3글자가 들어간다면 +3이 됐었기 때문에 -2를 시켜준다
            # 따라서 글자길이수 -1 만큼 빼줌
            answer -= len(j)-1
            temp = ''
            
print(answer)