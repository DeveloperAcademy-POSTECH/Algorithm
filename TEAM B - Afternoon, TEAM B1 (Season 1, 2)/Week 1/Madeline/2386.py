
while(1):
    cnt = 0
    length = 0
    stringInput = input()
    charInput = stringInput[0]
    if(charInput == "#"):
        break
    length = len(stringInput)
    for i in range(length):
        if (stringInput[i] == charInput) or (stringInput[i].lower() == charInput):
            cnt+=1
    print(charInput, cnt-1)