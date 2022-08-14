def negamax(curBoard, alpha=-22, beta=22, m='s', debug=False):
    pmoves = curBoard.playableMoves()
    nextBoards = [curBoard.playMove(col) for col in pmoves]

    evals = []
    best = [0, alpha]
    for i in range(len(pmoves)):
        board = nextBoards[i]
        move = pmoves[i]
        score = alpha
        end = False
        if board.moves == 42:
            score = 0
        elif board.checkWon():
            score = board.nbmoves()
            end = True
        else:
            score = -negamax(board, -beta, -alpha, m + ', ' + str(move))[1]
        ev = [move, score]
        evals.append([*ev])
        if best[1] < ev[1]:
            best = ev
        if end:
            break

    if debug:
        print(m)
        print(*evals)
        curBoard.print()
    return best
