def solution(n, words):
    answer = []
    for i in range(1, len(words)):
        # index 앞 단어의 맨 뒤 char와 뒷 단어의 맨 앞 char 비교
        if words[i-1][-1] != words[i][0]:
            # %=나머지 , //=몫
            return [(i%n)+1, (i//n)+1]
        # 이전에 나왔던 단어들 slice하여 현재 단어와 비교
        word = words[:i]
        if words[i] in word:
            return [(i%n)+1, (i//n)+1]
    return[0,0]

print("결과 = ", solution(2, ["hello", "one", "even", "never", "row", "world", "draw", "even"]))