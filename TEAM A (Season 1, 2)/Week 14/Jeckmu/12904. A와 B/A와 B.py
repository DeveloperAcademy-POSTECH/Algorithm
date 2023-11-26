S = input()
T = input()

isReversed = False

while len(S) != len(T):
    if isReversed:
        if T[0] == "A":
            T = T[1:]
        else:   # T[0] == "B"
            T = T[1:]
            isReversed = False
    else:
        if T[len(T)-1] == "A":
            T = T[:-1]
        else:   # T[len(T)] == "B"
            T = T[:-1]
            isReversed = True

def reverseResult():
    for i in range(len(T)-1, -1, -1):
        if T[i] != S[(len(T)-1)-i]:
            print(0)
            return
    print(1)
    
def result():
    for i in range(len(T)):
        if T[i] != S[i]:
            print(0)
            return
    print(1)
    
if isReversed:
    reverseResult()
else:
    result() 