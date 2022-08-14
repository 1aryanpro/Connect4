import time
from bitboard import BitBoard
from negamax import negamax
from texttable import Texttable

states = open('./Test_L3_R1.txt').read().splitlines()
states = [list(map(int, d.split(' '))) for d in states]

benchmarks = Texttable()
benchmarks.set_cols_align(['l', 'r', 'r', 'r'])
benchmarks.set_deco(Texttable.BORDER | Texttable.VLINES)
benchmarks.add_row(['No.', 'Eval', 'True', 'Time'])


for i in range(5):
    [moves, TrueEv] = states[i]
    board = BitBoard.fromMoves(moves)
    start = time.time()
    [_, ev] = negamax(board, debug=False)
    end = time.time()
    dur = int((end - start)*1000)
    row = [i+1, TrueEv, ev, dur]
    benchmarks.add_row(row)

print(benchmarks.draw())
