import fileinput

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

df_list = []

for i in range(0, len(lines)):
    if i == 0:
        nbrs = [int(elem) for elem in lines[i].split(",")]
    elif lines[i] == '':
        pass
    else:
        df_list.append([int(elem) for elem in lines[i].split()])

bingo = []

for i in range(0, len(df_list), 5):
    list = []
    for j in range(i, i+5):
        list.append(df_list[j])
    bingo.append(list)

marked = [[[False]*len(bingo[0][0]) for elem in bingo[0]] for row in bingo]


def sum_column(board, col):
    col_sum = 0
    for i in range(0, len(board[0])):
        col_sum += board[i][col]
    return col_sum


def sum_bingo(board, marked):
    board_sum = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if not marked[i][j]:
                board_sum += board[i][j]
    return board_sum


# PART I

find = False

for elem in nbrs:
    if not find:
        for i in range(0, len(bingo)):  # for every board
            for j in range(0, len(bingo[0])):  # for every row in board
                if elem in bingo[i][j]:
                    idx = bingo[i][j].index(elem)
                    marked[i][j][idx] = True
                if sum(marked[i][j]) == 5:
                    print('Bingo! Score: ', elem * sum_bingo(bingo[i], marked[i]))
                    find = True
                    break
            for k in range(0, len(bingo[0])): # for evert col in board
                if sum_column(marked[i], k) == 5:
                    print('Bingo! Score: ', elem * sum_bingo(bingo[i], marked[i]))
                    break
    else:
        break


# PART II
boards = [i for i in range(0, len(bingo))]
marked2 = [False for i in range(0, len(bingo))]
marked = [[[False]*len(bingo[0][0]) for elem in bingo[0]] for row in bingo]
find = False

for elem in nbrs:
    if not find:
        for i in range(0, len(bingo)):  # for every board
            if sum(marked2) < len(bingo):
                for j in range(0, len(bingo[0])):  # for every row in board
                    if elem in bingo[i][j]:
                        idx = bingo[i][j].index(elem)
                        marked[i][j][idx] = True
                    if sum(marked[i][j]) == 5:
                        marked2[i] = True
                        if len(boards) > 1 and i in boards:
                            boards.remove(i)
                for k in range(0, len(bingo[0])):  # for evert col in board
                    if sum_column(marked[i], k) == 5:
                        marked2[i] = True
                        if len(boards) > 1 and i in boards:
                            boards.remove(i)
            else:
                print('Bingo! Score: ', elem * sum_bingo(bingo[boards[0]], marked[boards[0]]))
                find = True
                break
    else:
        break

