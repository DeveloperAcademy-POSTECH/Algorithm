# https://www.acmicpc.net/problem/1158
# 백준-1158-요세푸스 문제

from collections import deque

n, k = map(int, input().split())
d = deque([str(num) for num in range(1, n+1)])
answer = []
while d:
    d.rotate(-(k-1))
    answer.append(d.popleft())
    
print(f"<{', '.join(answer)}>")
'''
k-1만큼 반시계방향으로 돌려서 k번째 값이 가장 처음에 오도록 하고, popleft 매서드로 그 값을 빼내어 answer에 순서대로 넣습니다.

'그냥 list로 선언하고 k번째 값을 pop으로 제거하면 되지 않느냐'라고 할 수 있지만 파이썬 list에서는 중간에 값을 삭제하거나 삽입할 경우 O(n)의 시간복잡도가 발생합니다.
단순히 하나의 원소에 대해서만 작업을 수행하는 것이 아닌 전체 원소를 다 작업해야 하기 때문이죠.

반면에 deque로 rotate를 돌릴 경우 rotate(k)에 대해서 O(k), popleft()의 경우 O(1)의 시간복잡도를 갖습니다.
list의 경우에도 가장 마지막 값을 pop할 경우 시간복잡도가 O(1)이라 숫자를 역순으로 넣고 마지막 값을 제거하는 방식으로 구현해도 되겠지만 list의 경우
rotate를 구현하려면 모든 원소를 수정해야 해서 O(n)의 시간복잡도를 가질 것이고, 따라서 n >> k의 경우에 차이가 꽤 날 것이라 생각합니다.
'''