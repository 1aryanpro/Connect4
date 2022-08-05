import curses


class Board:
    def __init__(self, cols, lines):
        self.state = [[0 for y in range(6)] for x in range(7)]
        self.tops = [0 for x in range(7)]
        self.x = int(cols / 2 - 6)
        self.y = int(lines / 2 - 4)
        self.selected = 0
        self.curr = 1
        self.winner = None
        self.gameOver = False

    def draw(self, stdscr):

        turnstr = "Player " + str(self.curr) + "'s Turn"
        stdscr.addstr(self.y - 4, self.x - 1, turnstr,
                      curses.color_pair(self.curr))

        for col in range(7):
            x = col * 2 + self.x

            selectedCol = col == self.selected
            if selectedCol:
                stdscr.addch(self.y - 1, x, '↓', curses.color_pair(self.curr))

            for row in range(6):
                y = 5 - row + self.y

                piece = self.state[col][row]
                ch = "◯" if piece == 0 else "●"

                selectedRow = row == self.tops[col]
                colorid = self.curr if selectedRow and selectedCol else piece
                color = curses.color_pair(colorid)

                stdscr.addch(y, x, ch, color)

        if self.gameOver:
            stdscr.addstr(self.y - 10, self.x - 2, "Winner is Player " +
                          str(self.winner), curses.color_pair(self.winner))

    def right(self):
        if (self.selected < 6):
            self.selected += 1

    def left(self):
        if (self.selected > 0):
            self.selected -= 1

    def down(self):
        top = self.tops[self.selected]
        if (top == 6):
            return
        self.state[self.selected][top] = self.curr
        self.tops[self.selected] += 1
        self.checkWin()
        self.curr = 1 if self.curr == 2 else 2

    def checkWin(self):
        cur = self.curr
        vcount = 0
        hcounts = [0] * 6

        # vertical connects
        for x in range(7):
            for y in range(6):
                p = self.state[x][y]
                if p == cur:
                    vcount += 1
                    hcounts[y] += 1
                else:
                    vcount = 0
                    hcounts[y] = 0

                if vcount == 4 or hcounts[y] == 4:
                    self.winner = cur
                    self.gameOver = True
                    self.selected = -1


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    board = Board(curses.COLS, curses.LINES)
    board.draw(stdscr)

    key = ''
    while not board.gameOver:

        key = stdscr.getkey()
        if key == 'KEY_RIGHT' or key == 'd' or key == 'l':
            board.right()
        elif key == 'KEY_LEFT' or key == 'a' or key == 'h':
            board.left()
        elif key == 'KEY_DOWN' or key == 's' or key == 'j':
            board.down()

        if key == 'q':
            return

        stdscr.erase()
        stdscr.addstr(2, 2, key, curses.color_pair(2))

        board.draw(stdscr)

    while True:
        board.draw(stdscr)
        if stdscr.getkey() == 'q':
            return


curses.wrapper(main)
