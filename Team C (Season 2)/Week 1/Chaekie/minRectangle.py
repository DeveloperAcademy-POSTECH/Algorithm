def solution(sizes):
    max_in_max = 0
    max_in_min = 0

    for size in sizes:
        if max(size) > max_in_max:
            max_in_max = max(size)
        if min(size) > max_in_min:
            max_in_min = min(size)

    answer = max_in_max * max_in_min
    return answer