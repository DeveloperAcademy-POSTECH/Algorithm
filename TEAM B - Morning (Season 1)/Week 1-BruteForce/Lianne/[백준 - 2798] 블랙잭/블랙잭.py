

cardNum, targetCardNum = map(int, input().split())
cardList = list(map(int, input().split()))
sumList = []

for i in range(cardNum - 2):
    for j in range(i + 1, cardNum - 1):
        for k in range(j + 1, cardNum):
            sum = cardList[i] + cardList[j] + cardList[k]
            
            if sum < targetCardNum or sum == targetCardNum:
               sumList.append(sum)

print(max(sumList))


