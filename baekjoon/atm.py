N = int(input())

for i in range(0, 1):
    # 리스트 형태로 int split해서 받아옴
    P = list(map(int, input().split(' ')))

# sort()를 통해 오름차순 정렬
P.sort()

answer = 0

# P[0:i] 하는 것이기 때문에 1번부터 시작 > [0:1] // 1부터 시작했으니 N+1
for i in range(1, N+1):
    # 리스트 0번쨰부터 i번째까지 더한것을 answer에 계속 더해줌
    answer += sum(P[0:i])
    
print(answer)