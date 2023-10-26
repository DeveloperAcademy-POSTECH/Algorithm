def solution(players, callings):
    list1 = {k:v for k,v in enumerate(players)}
    list2 = {v:k for k,v in enumerate(players)}
    for call in callings:
      # 인덱스 번호 탐색
        index = list2.get(call)
        prePlayer = list1.get(index-1)
        list1.update({index-1:call, index:prePlayer})
        list2.update({call:index-1, prePlayer:index})
    
    return list(list1.values())