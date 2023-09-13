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


# 처음 풀이 -> 시간초과
def solution2(players, callings):
    for calling in callings:
        for idx, player in enumerate(players):
            if calling == player:
                players[idx], players[idx -1] = players[idx -1], players[idx]
    return players