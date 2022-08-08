class C4Board:
    def __init__(self, state=0, mask=0, moves=0):
        self.state = state
        self.mask = mask
        self.moves = moves

    def copy(self):
        return C4Board(self.state, self.mask, self.moves)


def playMove(board, col):
    if not canPlay(board, col):
        return
    board.state ^= board.mask
    board.mask |= board.mask + bot_mask(col)
    board.moves += 1


def canPlay(board, col):
    return board.mask != board.mask | top_mask(col)


def boardFromMoves(moves):
    board = C4Board()
    moves = str(moves)
    for m in moves:
        p = int(m) - 1
        playMove(board, p)

    printBoard(board.state, board.mask)

    # print('state:')
    # printBits(board.bitState)
    # print('mask:')
    # printBits(board.mask)

    return board


def top_mask(col):
    return (1 << 5) << col * 7


def bot_mask(col):
    return 1 << col*7


def col_mask(col):
    return ((1 << 7) - 1) << col*7


def printBits(num):
    cols = list((num >> i) & 0x7F for i in range(0, 49, 7))
    colStrs = []
    for col in cols:
        colStrs.append(format(col, '06b'))

    for i in range(6):
        ps = ''
        for c in colStrs:
            ps += c[i]
        print(ps)


def printBoard(bits, mask):
    P1 = '\033[0;31m'
    P2 = '\033[0;33m'
    EM = '\033[0;39m'

    bcols = list((bits >> i) & 0x7F for i in range(0, 49, 7))
    mcols = list((mask >> i) & 0x7F for i in range(0, 49, 7))

    # for mcol in mcols:
    #     print(format(mcol, 'b'))

    boardStrs = [''] * 6
    for y in range(6):
        for x in range(7):
            m = (mcols[x] >> y) & 1
            b = (bcols[x] >> y) & 1
            boardStrs[y] += (P2 + 'o' if b else P1 +
                             'x' if m else EM + '.') + ' '
    boardStrs = boardStrs[::-1]

    for b in boardStrs:
        print(b)


board = boardFromMoves(2252576253462244111563365343671351441)
