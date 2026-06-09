
li = [1,2,3,4,5,6,7,8,9]
wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
print("\n\tTIC TAC TOE")
player = 'X'
flag = 0
count = 0
def show(x):
    if isinstance(x, int):
        return ' '
    return x
while True:
    print(f"\n\t {show(li[0])} | {show(li[1])} | {show(li[2])}")
    print("\t-----------")
    print(f"\t {show(li[3])} | {show(li[4])} | {show(li[5])}")
    print("\t-----------")
    print(f"\t {show(li[6])} | {show(li[7])} | {show(li[8])}")
    if flag==1:
        break
    if count==9:
        print("\n\tMATCH TIES")
        break
    ch = int(input(f"\n     Player {player} Turns : "))
    if ch in li:
        li[ch-1] = player
        count+=1
        for a,b,c in wins:
            if li[a]==li[b]==li[c]:
                print(f"\tPlayer {player} Wins")
                flag = 1
        if player=='X':
            player='O'
        else:
            player='X'
    else:
        print("\n\t Alredy Chosen")
