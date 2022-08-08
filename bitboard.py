class BitBoard:
    def __init__(self):
        self.curr = 1
        self.winner = None
        self.gameOver = False
        self.bitState = 0
        self.mask = 0
        self.moves = 0

    @staticmethod
    def fromMoves(moves):
        board = BitBoard()
        moves = str(moves)
        for m in moves:
            p = int(m) - 1
            board.playMove(p)

        printBoard(board.bitState, board.mask)

        # print('state:')
        # printBits(board.bitState)
        # print('mask:')
        # printBits(board.mask)

        return board

    def playMove(self, col):
        if self.cantPlay(col):
            return
        self.bitState ^= self.mask
        self.mask |= self.mask + bot_mask(col)
        self.moves += 1
        pass

    def cantPlay(self, col):
        return self.mask == self.mask | top_mask(col)


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
