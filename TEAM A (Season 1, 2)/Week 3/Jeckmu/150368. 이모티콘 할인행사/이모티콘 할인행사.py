import sys
sys.setrecursionlimit(10000)
def solution(users, emoticons):
    # 할인율의 중복조합
    d = [10, 20, 30, 40]
    discounts = []


    def p(arr, depth, l):
        if depth == l:
            discounts.append(arr)
            return

        for i in range(4):
            p(arr+[d[i]], depth+1, l)


    # 할인율 리스트 생성
    p([], 0, len(emoticons))

    # 최종 결과.
    answer = [0, 0]

    # 모든 할인율 리스트에 대해 모든 유저의 상황을 확인, 최적의 상황 탐색
    for discount in discounts:
        # 각 할인율 리스트에 대한 총 이모티콘 플러스 가입 유저와 이모티콘 구매 비용
        emo_plus = 0
        emo_total = 0

        for user in users:
            total = 0
            # 각 유저에 대해 각 아이템의 할인율을 대조하여, 살 지 말 지 확인.
            for i in range(len(discount)):
                # 이모티콘의 할인율이 유저가 생각하던 비율보다 높다면 구매
                if user[0] <= discount[i]:
                    total += int(emoticons[i]*((100-discount[i]))/100)

            # 유저가 설정한 가격 이상일 시, 이모티콘 플러스 가입. 아니라면, 이모티콘 총 구매 비용에 합산.
            if total >= user[1]:
                emo_plus += 1
            else:
                emo_total += total

        # 이모티콘 가입자가 더 많다면 무조건 값 대체
        if answer[0] < emo_plus:
            answer = [emo_plus, emo_total]
        # 이모티콘 가입자가 이전과 같다면, 총 판매 비용이 높을 때만 값 대체
        elif answer[0] == emo_plus:
            if answer[1] <= emo_total:
                answer = [emo_plus, emo_total]
    return answer