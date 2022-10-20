def solution(n):
    
    n_list = []

    for i in range(len(n)):
        if not n_list:
            n_list.append(n[i])
        else:
            if n[i] == n_list[-1]:
                n_list.pop()
            else:
                n_list.append(n[i])
                
    if n_list:
        return 0
    else:
        return 1

print("결과 : {}".format(solution("baabact")))