
# 베스트 앨범
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
from typing import List

def solution(genres: List[str], plays: List[int]) -> List[int]:
    song_dict = {}
    TOTAL_PLAY = "total_play"
    SONGS = "songs"
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre in song_dict:
            song_dict[genre][TOTAL_PLAY] += play
            song_dict[genre][SONGS] += [(play, i)]
        else:
            song_dict[genre] = {}
            song_dict[genre][TOTAL_PLAY] = play
            song_dict[genre][SONGS] = [(play, i)]
            
    answer = []

    for genre, genre_dict in sorted(song_dict.items(), key=lambda item: item[1][TOTAL_PLAY], reverse=True):
        sorted_songs = sorted(genre_dict[SONGS], key=lambda x: x[0], reverse=True)
        target_songs = sorted_songs[:min(len(genre_dict[SONGS]), 2)]
        additional_songs = [trackNum for _, trackNum in target_songs]
        answer += additional_songs
    
    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres=genres, plays=plays))