# https://www.acmicpc.net/problem/1987
# 백준-1987-알파벳

'''
우선 이 문제는 결과적으로 풀지 못했습니다. 시간 초과가 계속 나더라고요.
그래도 다른 분들과 함께 고민해보고 싶어서 넣었습니다.

저는 아직도 이 문제의 시간복잡도에 대해 정확히 알지 못하는데요. 제일 아래에 시간복잡도에 대해 생각해본 과정을 적어놓을테니 다른 분들도 한번 고민해보시고 얘기 나누면 좋을 것 같습니다.
'''

# 풀이1
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
alphabets = []
for _ in range(r):
    alphabets.append(list(input().rstrip()))
    
counts = [[0 for _ in range(c)] for _ in range(r)]
counts[0][0] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque( [(0, 0, [alphabets[0][0]])] )
while q:
    x, y, storage = q.popleft()
    for k in range(4):
        next_x, next_y = x + dx[k], y + dy[k]
        if 0 <= next_x < c and 0 <= next_y < r and alphabets[next_y][next_x] not in storage:
            q.append((next_x, next_y, storage+[alphabets[next_y][next_x]]))
            counts[next_y][next_x] = max(counts[next_y][next_x], counts[y][x] + 1)

print(max([max(row) for row in counts]))
'''
문제를 봤을 때 딱 떠오르는 것은 dfs였지만 bfs로 시도해보고 싶었습니다. 하지만 대차게 실패.
'''

# 풀이2
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
alphabets = []
for _ in range(r):
    alphabets.append(list(input().rstrip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

max_count = 0
storage = [alphabets[0][0]]
stack = [(0, 0, storage, 1)]
while stack:
    x, y, storage, count = stack.pop()
    max_count = max(max_count, count)
    if max_count == 26:
        break
    for k in range(4):
        next_x, next_y = x + dx[k], y + dy[k]
        if 0 <= next_x < c and 0 <= next_y < r and alphabets[next_y][next_x] not in storage:
            stack.append((next_x, next_y, storage+[alphabets[next_y][next_x]], count+1))
            
print(max_count)
'''
위와 유사하지만 dfs로 시도해봤습니다. 역시 시간초과가 뜹니다.
alphabets[next_y][next_x] not in storage -> 이 부분은 len(storage)만큼 연산을 수행합니다. 이 부분이 문제인 것 같았습니다.
질문 게시판을 뒤적이며 저 부분의 시간복잡도를 O(1)로 만들 방법을 고민했습니다. 
'''

# 풀이3
import sys

input = sys.stdin.readline

def dfs(x, y, count):
    global max_count
    max_count = max(max_count, count)
    for idx in range(4):
        next_x, next_y = x + dx[idx], y + dy[idx]
        if 0 <= next_x < c and 0 <= next_y < r and is_visited[ord(alphabets[next_y][next_x])-65] == False:
            is_visited[ord(alphabets[next_y][next_x])-65] = True
            dfs(next_x, next_y, count+1)
            is_visited[ord(alphabets[next_y][next_x])-65] = False
          
r, c = map(int, input().split())
alphabets = []
for _ in range(r):
    alphabets.append(list(input().rstrip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

is_visited = [False for _ in range(26)]
is_visited[ord(alphabets[0][0])-65] = True
        
max_count = 1

dfs(0, 0, 1)

print(max_count)
'''
dfs입니다.
global 변수로 max_count를 선언하여 변화를 추적할 수 있게 하고, is_visited에 길이가 26이고 원소들이 모두 Bool 값인 list를 할당했습니다.
ord()를 통해 'A~Z'를 숫자로 변환하고 그 값의 범위를 0~25로 만들어 index로 활용했습니다.
if문 내에서 해당 알파벳이 이미 탐색되었는지 판단할 때 indexing이 이루어지는데 연산횟수는 1번입니다.
이 방법으로 문제를 해결할 수 있다고 생각했지만 시간초과가 떴습니다.
'''

'''
처음에 문제를 접했을 때 rough하게 최악의 경우 3^26번의 연산이 발생할거라 생각했습니다. 기본적으론 상하좌우 네 방향으로 움직일 수 있는데 이미 지나온 곳은 갈 수 없으므로
3가지 방향으로 향할 수 있다고 생각했습니다. 이미 지나온 알파벳은 다시 지날 수 없으므로 알파벳 개수인 26이 최대 길이라고 생각했고요.

그 다음엔 조금 더 정확하게 파악해보려 했습니다. 처응 위치는 고정이므로 1번째의 이동 가능한 선택지는 1개뿐이죠. 그리고 (0,0) 위치에서 시작하므로 2번째 선택지는
오른쪽 혹은 아래쪽, 2가지뿐입니다. 1 * 2 * 3^24 = 2 * 3^24 라고 생각했습니다. 실제로는 이보다 적을 것입니다. 테두리 부분에서 이동할 경우 이미 지나온 위치,
범위를 넘어 갈 수 없는 위치 2가지가 빠지므로 2가지의 선택지밖에 없죠.

테두리 근방이 아니라 중심부로 가서 사방에 이동할 수 있는 공간이 충분히 있을 때에도 실제로는 매번 3가지 선택지가 주어지진 않습니다.
'X'가 이미 지나온 지점, '(X)'가 현재 위치, 'O'가 이동 가능한 지점이라고 가정하고 경로를 그려보겠습니다. 그 외의 지점은 편의상 나타내지 않겠습니다.

X X X
    X
    X
  O(X)O
    O

일단 왼쪽, 오른쪽, 아래의 3가지 위치로 이동이 가능합니다. 그 다음은 어떨까요

X X X
    X
  O X O
O X X X O
  O X O
    O

이전에 이동가능했던 3가지 위치에 대해 각각 또다시 3가지 이동이 가능해 3^2 = 9가지의 이동가능한 지점이 있을거라 생각했지만 그렇지 않습니다.
겹치는 지점이 있기 때문이죠. 
여기서 한번 더 같은 방식으로 전개했을 떄 그 가짓수 또한 3^3 = 27이 아닙니다. 겹치는 지점도 나타날 거고 이미 지나온 지점이라 갈 수 없는 경우도 있겠죠.

설명이 길었네요. 정리하자면 '아주 rough하게 생각했을 땐 최악의 경우 3^26번의 연산횟수를 갖지만 실제로는 그에 못 미치는 연산횟수를 갖는다'입니다.
근데 그 정확한 수치를 모르겠어요. 
질문 게시판의 어떤 분은 2^26가 최악의 연산 횟수라고 적어놓으셨던데 동의하지 못하겠습니다. (아마도) 매 순간 이동 가능한 지점이 오른쪽 혹은 아래의 2가지 경우라고 생각하여 
그런 값이 나온 것 같은데 예시를 생각해보면 위나 왼쪽으로 이동했을 때 그 경로가 최대 길이를 갖는 경우도 있거든요.

어쩌면 제가 사고의 전개를 처음부터 잘못한 것일지도 모릅니다. 이 글을 가장 아래에 쓴 이유가 다른 분들은 혹시 틀렸을지도 모를 제 사고 과정을 따르지 않고
각자 생각해보시기를 바랐기 떄문입니다. 이 문제의 시간 복잡도와 관련해서 아이디어가 있으면 언제든지 연락주세요..!
'''