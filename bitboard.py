class BitBoard:
    def __init__(self, state=0, mask=0, moves=0):
        self.state = state
        self.mask = mask
        self.moves = moves

    def copy(self):
        return BitBoard(self.state, self.mask, self.moves)

    def playMove(self, col):
        if not self.canPlay(col):
            return
        self.mask |= self.mask + bot_mask(col)
        self.moves += 1
        self.state ^= self.mask

    def canPlay(self, col):
        return self.mask != self.mask | top_mask(col)

    def playableMoves(self):
        cols = []
        for i in range(7):
            if self.canPlay(i):
                cols.append(i)
        return cols

    @staticmethod
    def fromMoves(moves):
        board = BitBoard()
        moves = str(moves)
        for m in moves:
            p = int(m) - 1
            board.playMove(p)
        return board

    def checkAligned(self):
        bits = self.state

        def testDir(func):
            fbits = func(bits)
            doubles = bits & fbits
            ffdoubles = func(func(doubles))
            doubles = doubles & ffdoubles
            if doubles > 0:
                return True
            return False

        verti = testDir(lambda b: b >> 1)
        horiz = testDir(lambda b: b >> 7)
        diag1 = testDir(lambda b: b >> 6)
        diag2 = testDir(lambda b: b >> 8)

        if verti or horiz or diag1 or diag2:
            return True
        return False

    def print(self):
        bits = self.state if self.moves & 1 else self.state ^ self.mask
        mask = self.mask

        P1 = '\033[0;31mo '
        P2 = '\033[0;33mx '
        EM = '\033[0;39m. '

        bcols = list((bits >> i) & 0x7F for i in range(0, 49, 7))
        mcols = list((mask >> i) & 0x7F for i in range(0, 49, 7))

        boardStrs = [''] * 6
        for y in range(6):
            for x in range(7):
                m = (mcols[x] >> y) & 1
                b = (bcols[x] >> y) & 1
                boardStrs[y] += P2 if b else P1 if m else EM
        boardStrs = boardStrs[::-1]

        print('\n'.join(boardStrs))
        print('\033[0;39m')


def top_mask(col):
    return (1 << 5) << col * 7


def bot_mask(col):
    return 1 << col*7


def col_mask(col):
    return ((1 << 7) - 1) << col*7


def printBits(num):
    P1 = '\033[0;31m'
    EM = '\033[0;39m'

    bcols = list((num >> i) & 0x7F for i in range(0, 49, 7))

    boardStrs = [''] * 6
    for y in range(6):
        for x in range(7):
            b = (bcols[x] >> y) & 1
            boardStrs[y] += P1 if b else EM
            boardStrs[y] += '1' if b else '0'
    boardStrs = boardStrs[::-1]

    print('\n'.join(boardStrs))
    print(EM)


board = BitBoard.fromMoves(2252576253462244111563365343671351441)
board.print()
