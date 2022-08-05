import curses


class Board:
    def __init__(self, cols, lines):
        self.state = [[0 for y in range(6)] for x in range(7)]
        self.tops = [0 for x in range(7)]
        self.x = int(cols / 2 - 6)
        self.y = int(lines / 2 - 4)
        self.selected = 0
        self.curr = 1

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
        self.curr = 1 if self.curr == 2 else 2
        self.checkWin()

    def checkWin(self):
        pass


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    board = Board(curses.COLS, curses.LINES)

    key = ''
    while True:
        stdscr.erase()

        if key == 'KEY_RIGHT' or key == 'd':
            board.right()
        elif key == 'KEY_LEFT' or key == 'a':
            board.left()
        elif key == 'KEY_DOWN' or key == 's':
            board.down()

        stdscr.addstr(2, 2, key, curses.color_pair(2))

        board.draw(stdscr)
        key = stdscr.getkey()


curses.wrapper(main)
key = stdscr.getkey()


curses.wrapper(main)
key = stdscr.getkey()


curses.wrapper(main)
