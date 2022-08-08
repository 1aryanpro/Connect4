class C4Board:
    def __init__(self):
        self.state = [[0 for y in range(6)] for x in range(7)]
        self.tops = [0 for x in range(7)]
        self.curr = 1
        self.winner = None
        self.gameOver = False

    @staticmethod
    def fromMoves(moves):
        board = C4Board()
        moves = str(moves)
        for m in moves:
            p = int(m) - 1
            board.playMove(p)
        return board

    def playMove(self, pos):
        top = self.tops[pos]
        if (top == 6):
            return
        self.state[pos][top] = self.curr
        self.tops[pos] += 1
        self.checkWin(pos)
        self.curr = 1 if self.curr == 2 else 2

    def checkWin(self, mx):
        my = self.tops[mx] - 1
        cur = self.curr

        vcount = 0
        for y in range(6):
            p = self.state[mx][y]
            if p == cur:
                vcount += 1
            else:
                vcount = 0

            if vcount == 4:
                self.winner = cur
                self.gameOver = True
                self.selected = -1
                return

        hcount = 0
        for x in range(7):
            p = self.state[x][my]
            if p == cur:
                hcount += 1
            else:
                hcount = 0

            if hcount == 4:
                self.winner = cur
                self.gameOver = True
                self.selected = -1
                return
