# N 개의 랜선을 만들어야함
# 이미 K 개의 랜선을 갖고 있지만, 랜선의 길이가 제각각
# 모두 N 개의 같은 길이의 랜선으로 만들고 싶어서, K 개의 랜선을 잘라서 만들어야함

# K 개의 랜선으로 N 개의 랜선을 만들 수 없는 경우는 없음
# N 개보다 많이 만드는것도 N 개에 포함

# 만들 수 있는 최대 랜선의 길이를 구해야함

# K <= 10,000, N < 1,000,000

# 여기에 이분탐색을 어떻게 적용함???? 그리고 어떻게 여기서 이분탐색이 떠오르지?
# -> 랜선의 길이가 터무니없음. 2^31-1 이면 말도 안되게 큰 수니까 이분탐색으로 해야겠다 라는 생각을 해야함

# 그래도 방법이 모르겠어서 답을 찾아봄
# https://jjini-3-coding.tistory.com/11
# 여기서 보면 1이 start 고 최장길이의 랜선이 end
# 이제 이 상태에서 mid 를 구해서 각각 직접 몇개의 랜선이 나오는지 계산
# 만약 갯수보다 적게 나온다? -> start 를 start, mid 를 end 로 놓음
# 만약 갯수보다 많이 나온다? -> start 를 mid, end 를 end 로 놓음
# 이 상태로 계속 돌려서 가능한 제일 긴 길이의 랜선을 구할때까지 돌림
# 함 해보자

import sys

sys.stdin = open("1654_lineCutting/lineCutting.txt")

K, N = map(int, sys.stdin.readline().split())

lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

# 이진 탐색 시작
# 우선은 start 와 end 를 만듬
start = 1
end = max(lines)
mid = 0
answer = 0
while start <= end: # start 가 end 를 넘어가는 순간 이진탐색 종료
    mid = (start + end) // 2 # 가운데 값 찾기
    cnt = 0 # 랜선 몇개 나오는지 세는 변수

    for i in range(K): # 랜선 자르기 시도
        cnt += lines[i] // mid
    
    if cnt < N: # 랜선수가 적게 나왔다? -> 자를려고 시도하는 랜선의 길이를 줄인다 -> mid 값을 낮춰야하니까 start 를 start 로, end 를 mid - 1 로
        end = mid - 1
    else: # 랜선수가 더 많이 나왔다? -> 랜선의 길이를 늘려서 최장 길이가 되는지 보자 -> mid 를 올리자 -> start 를 mid + 1 로 end 를 end 로
        answer = mid
        start = mid + 1

print(answer)

