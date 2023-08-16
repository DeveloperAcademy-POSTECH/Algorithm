# 입력
schedule = []
n = int(input())
for i in range(n):
    start, end = map(int, input().split())
    schedule.append((start, end))

# 정렬 기준 1 : end가 빠른 순서 => item[1]을 기준으로 오름차순 정렬
schedule.sort(key = lambda x: x[1])

# 정렬기준 2 : start가 빠른 순서 => item[0]의 오름차순 정렬
schedule.sort(key = lambda x: x[0])

# cnt
cnt = 1 # 일단 첫번째 회의는 무조건 들어가기 때문에 count 초기값은 1

# 배열에서 앞 요소의 end타임보다 뒷 요소의 start 타임이 크거나 같으면 count

before_end = schedule[0][1] # before_end의 초기값은 schedule[0][1]


for i in range(1,n) :
    if schedule[i][1] <= before_end :
        cnt += 1
        # 비교 대상인 item이 count가 되는 경우에만 before_end로 갱신.
        before_end = schedule[i][1]

print(cnt)