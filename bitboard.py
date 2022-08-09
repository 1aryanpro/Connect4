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
        self.state ^= self.mask
        self.mask |= self.mask + bot_mask(col)
        self.moves += 1

    def canPlay(self, col):
        return self.mask != self.mask | top_mask(col)

    @staticmethod
    def fromMoves(moves):
        board = BitBoard()
        moves = str(moves)
        for m in moves:
            p = int(m) - 1
            board.playMove(p)
        return board

    def print(self):
        bits = self.state
        mask = self.mask

        P1 = '\033[0;31mo '
        P2 = '\033[0;33mx '
        EM = '\033[0;39m. '

        bcols = list((bits >> i) & 0x7F for i in range(0, 49, 7))
        mcols = list((mask >> i) & 0x7F for i in range(0, 49, 7))

        boardStrs = [''] * 6
        print()
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
    cols = list((num >> i) & 0x7F for i in range(0, 49, 7))
    colStrs = []
    for col in cols:
        colStrs.append(format(col, '06b'))

    for i in range(6):
        ps = ''
        for c in colStrs:
            ps += c[i]
        print(ps)


board = BitBoard.fromMoves(2252576253462244111563365343671351441)
board.print()
