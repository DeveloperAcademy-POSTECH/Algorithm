def solution1(players, callings):
    answer = []
    rank_dict = {i: players[i] for i in range(len(players))}
    player_dict = {players[i]: i for i in range(len(players))}

    for calling in callings:
        current_rank = player_dict[calling]
        front_player = rank_dict[current_rank - 1]
        rank_dict[current_rank - 1] = calling
        rank_dict[current_rank] = front_player
        player_dict[calling] -= 1
        player_dict[front_player] += 1

    answer = list(rank_dict.values())    

    return answer



# dictionary 한개만 쓰기
def solution2(players, callings):
    pla_dic = {key: i for i, key in enumerate(players)}

    for calling in callings:
        rank = pla_dic[calling]
        pla_dic[calling] -= 1
        pla_dic[players[rank-1]] += 1
        players[rank-1], players[rank] = players[rank], players[rank-1]

    return players


# 처음 풀이 -> 시간초과
def solution3(players, callings):
    for calling in callings:
        for idx, player in enumerate(players):
            if calling == player:
                players[idx], players[idx -1] = players[idx -1], players[idx]
    return players

