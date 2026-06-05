import random

class stratghy:
    win = 25
    not_lost = 75

dic_teach = eval(open('amoz_XO.txt' , 'r').read())
moved = eval(open('moved.txt' , 'r').read())

def add_mat(mat):
    global dic_teach
    dic_move = {}
    for move in mat_to_list_moved(mat):
        dic_move[move] = {'win':0 , 'tasavi':0 , 'play':0}
    dic_teach[str(mat)] = dic_move

def choice_moved(mat):
    global dic_teach
    if str(mat) not in dic_teach.keys():
        return random.choice(mat_to_list_moved(mat))
    list_move = dic_teach[str(mat)]
    list_moved = []
    n = -1
    for move in list_move:
        kefit = 0
        if list_move[move]['play'] != 0:
            kefit = (list_move[move]['win'] * stratghy.win + (list_move[move]['tasavi']) * stratghy.not_lost) / (list_move[move]['play'] * 100)
        if kefit > n:
            n = kefit
            list_moved = [move]
        elif kefit == n:
            list_moved += [move]
    return random.choice(list_moved)

def is_win(x , o):
    if len(x) < 3 and len(o) < 3:
        return False
    if (0 , 0) in x and (1 , 1) in x and (2 , 2) in x:
        return 'x'
    if (0 , 0) in o and (1 , 1) in o and (2 , 2) in o:
        return 'o'
    if (0 , 2) in x and (1 , 1) in x and (2 , 0) in x:
        return 'x'
    if (0 , 2) in o and (1 , 1) in o and (2 , 0) in o:
        return 'o'
    for i in range(3):
        if (0 , i) in x and (1 , i) in x and (2 , i) in x:
            return 'x'
        if (0 , i) in o and (1 , i) in o and (2 , i) in o:
            return 'o'
        if (i , 0) in x and (i , 1) in x and (i , 2) in x:
            return 'x'
        if (i , 0) in o and (i , 1) in o and (i , 2) in o:
            return 'o'
    return False

def mat_to_list_moved(matris):
    listt = []
    for i in range(3):
        for j in range(3):
            if matris[i][j] == '':
                listt += [(i , j)]
    return listt

def teaching(play , win_T_F = 0):
    global dic_teach
    global moved
    if play not in moved:
        for mat in play.keys():
            if mat not in dic_teach.keys():
                add_mat(eval(mat))
            if win_T_F == 1:
                dic_teach[mat][play[mat]]['win'] += 1
            elif win_T_F == 0:
                dic_teach[mat][play[mat]]['tasavi'] += 1
            elif win_T_F == -1:
                continue
            dic_teach[mat][play[mat]]['play'] += 1
        moved.append(play)
    else:
        return ''
    open('amoz_prise.txt' , 'w').write(str(dic_teach))
    open('moved.txt' , 'w').write(str(moved))


def play_teach(flag , value_teach = True):
    print('start')
    mat_x = [['' , '' , ''] , ['' , '' , ''] , ['' , '' , '']]
    mat_o = [['' , '' , ''] , ['' , '' , ''] , ['' , '' , '']]
    x_moved = {}
    o_moved = {}
    n = flag
    f = 1
    win = False
    while not win and f < 10:
        if n % 2 == 0:
            move = choice_moved(mat_x)
            print(f'sistem: {move}')
            x_moved[str(mat_x)] = move
            mat_x[move[0]][move[1]] = 'x'
            mat_o[move[0]][move[1]] = 'o'
        else:
            move = eval(input('your move: '))
            o_moved[str(mat_o)] = move
            mat_o[move[0]][move[1]] = 'x'
            mat_x[move[0]][move[1]] = 'o'
        n += 1
        f += 1
        win = is_win(x_moved.values() , o_moved.values())
    if win == 'x':
        if value_teach:
            teaching(o_moved , win_T_F=-1)
        print('lost')
    elif win == 'o':
        if value_teach:
            teaching(o_moved , win_T_F=1)
        print('win')
    else:
        if value_teach:
            teaching(o_moved , win_T_F=0)
        print('tasavi')
            

def main():
    global dic_teach
    global moved
    print('hello')
    n = 0
    while True:
        command = input('play teach(0)  play(1)  exit(2): ')
        if command == '2':
            break
        elif command == '1':
            play_teach(n , value_teach=False)
            n += 1
        elif command == '0':
            play_teach(n , value_teach=True)
            n += 1
        else:
            print('ERROR')
        open('amoz_prise.txt' , 'w').write(str(dic_teach))
        open('moved.txt' , 'w').write(str(moved))

main()