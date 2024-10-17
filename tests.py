import main
TOTAL=10
board = [
        ['O', 'X', 'O'],
        ['X', '-', '-'],
        ['X', 'O', '-']
    ]
#I tried this with a thousand an ten thousand,but the differences were pretty negligible
def test(playerX,playerO):
    results_total={'X':0,'O':0,'tie':0}
    test_number=1
    while test_number<=TOTAL:
        board = main.reset_board()
        result=main.play_game(board,playerX,playerO)
        results_total[result]+=1
        test_number+=1
    return results_total



def results_print(results):
    for trial in results:
        print(trial)

def test_board_generator():
    board = [
        ['O', 'X', 'O'],
        ['X', '-', '-'],
        ['X', 'O', '-']
    ]
    return board

if __name__=='__main__':
    results = [['random verses random',test('random','random')],
               ['basic verses random',test('basic','random')],
               ['random verses basic',test('random','basic')],
               ['basic versus basic',test('basic','basic')],
               ['advanced versus advanced',test('advanced','advanced')],
               ['advanced versus basic',test('advanced','basic')],
               ['basic verses advanced',test('basic','advanced')],
               ['random verses advanced', test('random', 'advanced')],
               ['advanced verses random', test('advanced', 'random')],
               ['plus verses advanced', test('plus', 'advanced')],
               ['advanced verses plus', test('advanced', 'plus')],
               ['minimax verses plus',test('minimax','plus10')]
               ]
    results_print(results)