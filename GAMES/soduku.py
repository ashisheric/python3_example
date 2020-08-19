input_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#Hint: for this I have using backtracking for each row, coloumn as well as 3*3 metrx i.e soduku box

def solve(bo):
    find = check_zero(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if verify(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def verify(bo, num, pos):
    # verify row of input board
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # verify coloumn of input board
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    # verify 3*3 metrix i.e soduku block
    pos_x = pos[1] // 3
    pos_y = pos[0] // 3

    for i in range(pos_y * 3, pos_y * 3 + 3):
        for j in range(pos_x * 3, pos_x * 3 + 3 ):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def check_zero(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j # i.e row and coloumn
    return None

def display_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("--------------------------------------")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8 :
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + "  ", end="")

display_board(input_board)
solve(input_board)
print("==============================================")
display_board(input_board)