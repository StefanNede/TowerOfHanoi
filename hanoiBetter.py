numMoves =0
def helper(n, start, via, end):
    global numMoves
    # return the action happening 
    if n == 1:
        numMoves +=1 
        return f"Move rock from {start} to {end}\n"

    moves = helper(n-1, start, end, via)
    moves += helper(1, start, via, end)
    moves += helper(n-1, via, start, end)
    return moves

def hanoi(n):
    return helper(n, 'A', 'B', 'C')


n = int(input())
print(hanoi(n))
print(f"Moves taken: {numMoves}")
