N = int(input())

times = []

for _ in range(N):
    start, end = map(int, input().split(" "))
    times.append((start, end))

# [(1, 2), (2, 3), (3, 6), (4, 6), (6, 9)] 이런 식으로 받아옴
# 시작 시간을 기준으로 오름차순으로 정렬
# 시작시간이 이전 시간의 종료시간보다 크면 +1
times.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = 0
for meeting in times:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1

print(answer)