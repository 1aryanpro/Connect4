import curses
from board import C4Board

board = C4Board.fromMoves(67255217565535272362732377313616611)
boardX = 0
boardY = 0
selected = 3


def drawBoard(stdscr):
    turnstr = "Player " + str(board.curr) + "'s Turn"
    stdscr.addstr(boardY - 4, boardX - 1, turnstr,
                  curses.color_pair(board.curr))

    for col in range(7):
        x = col * 2 + boardX

        selectedCol = col == selected
        if selectedCol:
            stdscr.addch(boardY - 1, x, '↓', curses.color_pair(board.curr))

        for row in range(6):
            y = 5 - row + boardY

            piece = board.state[col][row]
            ch = "◯" if piece == 0 else "●"

            selectedRow = row == board.tops[col]
            colorid = board.curr if selectedRow and selectedCol else piece
            color = curses.color_pair(colorid)

            stdscr.addch(y, x, ch, color)

    if board.gameOver:
        stdscr.addstr(boardY - 10, boardX - 2, "Winner is Player " +
                      str(board.winner), curses.color_pair(board.winner))


def moveSelected(m):
    global selected
    selected += m
    selected = max(min(selected, 6), 0)


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    global boardX, boardY
    cols = curses.COLS
    lines = curses.LINES
    boardX = int(cols / 2 - 6)
    boardY = int(lines / 2 - 4)

    drawBoard(stdscr)

    key = ''
    while not board.gameOver:

        key = stdscr.getkey()
        if key == 'l':
            moveSelected(1)
        elif key == 'h':
            moveSelected(-1)
        elif key == ' ':
            board.playMove(selected)

        if key == 'q':
            return

        stdscr.erase()
        stdscr.addstr(2, 2, key, curses.color_pair(2))

        drawBoard(stdscr)

    while True:
        drawBoard(stdscr)
        if stdscr.getkey() == 'q':
            return


curses.wrapper(main)
