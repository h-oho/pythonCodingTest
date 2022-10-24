word = input()
answer = 0

A = ["A","B","C"]
B = ["D","E","F"]
C = ["G","H","I"]
D = ["J","K","L"]
E = ["M","N","O"]
F = ["P","Q","R","S"]
G = ["T","U","V"]
H = ["W","X","Y","Z"]
    
for i in word:
    if i in A:
        answer += 3
    elif i in B:
        answer += 4
    elif i in C:
        answer += 5
    elif i in D:
        answer += 6
    elif i in E:
        answer += 7
    elif i in F:
        answer += 8
    elif i in G:
        answer += 9
    elif i in H:
        answer += 10
    
print(answer)