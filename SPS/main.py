import random
game_type = int(input("play Player or PC: "))
if game_type == 2:
    result_win_pc = 0
    result_win_pl = 0
    while True:
        pl_win = 0
        pc_win = 0
        while True:

            pl = int(input(" "))
            if pl == 1:
                print("k")
                break
            elif pl == 2:
                print("n")
                break
            elif pl == 3:
                print("b")
                break
            else:
                print("No simvol")
            if pc == 1:
                print("k")
            elif pc == 2:
                print("n")
            elif pc == 3:
                print("b")
        while True:

            pc = random.randint(1, 3)
            if pc > pl or pc == 3 and pc == 1:
                print("Computer win")
                pc_win += 1
            elif pc == pl:
                print("Draw")
            else:
                print("player win")
                pl_win += 1
            if pc_win == 3:
                print("win pc", pc_win , pl_win)
                break
                if pl_win == 3:
                    print("pl win", pl_win , pc_win)
                break
                print(f"win: ps ")
                a = input("Replay n/y?")
                if a != "y":
                    break
