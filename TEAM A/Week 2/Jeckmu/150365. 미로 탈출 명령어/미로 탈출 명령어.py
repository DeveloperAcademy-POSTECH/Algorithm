def solution(n, m, x, y, r, c, k):
    answer = ""

    # h = 최단거리길이
    h = abs(r-x) + abs(c-y)
    if k < h or (k-h) % 2 == 1:
        return 'impossible'

    down, left, right, up = 0, 0, 0, 0

    # d, l, r, u 최소 개수 저장
    if r-x > 0:
        down = r-x
    else:
        up = x-r

    if c-y > 0:
        right = c-y
    else:
        left = y-c

    move = k-h

    # down
    answer += "d"*down
    down = min(move//2, n-(x+down))
    answer += "d"*down
    up += down
    move -= 2*down

    # left
    answer += "l"*left
    left = min(move//2, y-left-1)
    answer += "l"*left
    right += left
    move -= 2*left

    # right, up
    answer += 'rl'*(move//2)    # 남은 movement를 rl로 대체
    answer += 'r'*right
    answer += 'u'*up

    return answer