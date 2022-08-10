from bitboard import BitBoard


def negamax(curBoard, alpha=-22, beta=22, m='s'):
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
            print('win')
            end = True
        else:
            score = negamax(board, -beta, -alpha, m + ', ' + str(move))[1]
        ev = [move, score]
        evals.append([*ev])
        if best[1] < ev[1]:
            best = ev
        if end:
            break
    best[1] *= -1

    print(m)
    print(*evals)
    curBoard.print()
    return best


board = BitBoard.fromMoves(7174362564676726631735257252323)
best = negamax(board)
best[1] *= -1

# print(board.moves)
print(best)
# board.print()
