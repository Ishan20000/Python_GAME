from turtle import Screen
from draw import Draw
from check import Check

check = Check()
my_screen = Screen()
my_screen.title("TIC-TAC-TOE")
my_screen.setup(650, 650)
draw = Draw()
my_screen.tracer(0)

total_moves = 0


def play(x, y):
    global total_moves
    end_check = 0
    is_game_on = True
    if is_game_on:
        z = draw.user_choice(x, y)
        option = str(z[0])
        player = z[1]
        check.new(option, player)
        my_screen.update()
        total_moves += 1
        end_check = check.game_over()
        if total_moves == 9:
            my_screen.textinput("Game over!", "Tie!")
            my_screen.bye()
        if end_check == 2:
            my_screen.textinput("Game over!", "X won!")
            my_screen.bye()
        if end_check == 1:
            my_screen.textinput("Game over!", "O won!")
            my_screen.bye()


my_screen.onclick(play)
my_screen.mainloop()
