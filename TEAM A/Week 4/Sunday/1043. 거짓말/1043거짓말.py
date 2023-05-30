import sys
input  = sys.stdin.readline
N,M = map(int,input().split())
peoplelist = list(map(int,input().split()))[1:]
uplist = [i for i in range(N+1)]

for i in peoplelist:
    uplist[i] = 0 #정답을 아는놈드은 0으로

def Union(a,b):
    x,y = find(a),find(b)
    if(x<y):
        uplist[y]=x
    else:
        uplist[x] = y
def find(x):
    if x == uplist[x]:
        return x
    return find(uplist[x])
party = []
for k in range(M):
    partylist = list(map(int,input().split()))[1:]
    party.append(partylist)
    for i in range(len(partylist)-1):
        Union(partylist[i],partylist[i+1])
        
ans = 0
for par in party:
    lie = True
    for i in par:
        if (find(i)==0):
            lie = False
            break
    if(lie == True):
        ans+=1
print(ans)