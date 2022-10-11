# tower of hanoi solution - uses DFS (not efficient)
inp = int(input("Enter number of stones: "))
lst = [i for i in range(1,inp+1)]
#print([lst,[],[]])
start = [lst,[],[]]
goal = [[],[],lst]

def getAvailableMoves(lst):
    possibilities = [] # will be a 2d array holding 2 arrays
    if len(lst[0]) >= 1:
        if len(lst[1]) == 0 or lst[0][0] < lst[1][0]:
            psb = [lst[0][1:], [lst[0][0]] + lst[1], lst[2]]
            possibilities.append(psb)
        if len(lst[2]) == 0 or lst[0][0] < lst[2][0]:
            psb = [lst[0][1:], lst[1], [lst[0][0]] + lst[2]]
            possibilities.append(psb)

    if len(lst[1]) >= 1:
        if len(lst[0]) == 0 or lst[1][0] < lst[0][0]:
            psb = [[lst[1][0]] + lst[0], lst[1][1:], lst[2]]
            possibilities.append(psb)
        if len(lst[2]) == 0 or lst[1][0] < lst[2][0]:
            psb = [lst[0], lst[1][1:], [lst[1][0]] + lst[2]]
            possibilities.append(psb)

    if len(lst[2]) >= 1:
        if len(lst[0]) == 0 or lst[2][0] < lst[0][0]:
            psb = [[lst[2][0]] + lst[0], lst[1], lst[2][1:]]
            possibilities.append(psb)
        if len(lst[1]) == 0 or lst[2][0] < lst[1][0]:
            psb = [lst[0], [lst[2][0]] + lst[1], lst[2][1:]]
            possibilities.append(psb)


    return possibilities

def hanoi(lst1, previousStates = [start], moves = 0, branchIgnored = []):
    if lst1 == goal:
        return previousStates, moves
    else:
        nList1 = getAvailableMoves(lst1)
        #print(branchIgnored)
        for subList in nList1:
            if subList not in previousStates:
                #print(f"{subList} --> {nList1}")
                return hanoi(subList,previousStates + [subList], moves+1, branchIgnored + nList1[1:])
        return hanoi(branchIgnored[-1], previousStates, moves+1, branchIgnored[:-1])

#print(getAvailableMoves([[], [1, 2, 3], []]))
solution, moves = hanoi(start)

print([lst,[],[]])
for step in solution:
    print(step)
print(f"Moves taken: {moves}")
