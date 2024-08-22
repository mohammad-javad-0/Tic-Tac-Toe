import tkinter as tk
from tkinter import messagebox


btn_list = [
    {"name": "btn_1", "function": lambda: play(0, 0, 0)},
    {"name": "btn_2", "function": lambda: play(1, 0, 1)},
    {"name": "btn_3", "function": lambda: play(2, 0, 2)},
    {"name": "btn_4", "function": lambda: play(3, 1, 0)},
    {"name": "btn_5", "function": lambda: play(4, 1, 1)},
    {"name": "btn_6", "function": lambda: play(5, 1, 2)},
    {"name": "btn_7", "function": lambda: play(6, 2, 0)},
    {"name": "btn_8", "function": lambda: play(7, 2, 1)},
    {"name": "btn_9", "function": lambda: play(8, 2, 2)},
]

root = tk.Tk()
root.title("Tic_Tac_Toe")
root.geometry("500x500")
root.resizable(False, False)
root.config(bg="#463838")
title_image = tk.PhotoImage(file="image/icon_title.png")
root.iconphoto(False, title_image)

map = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]


def reset_game():
    global map, turn
    map = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    lbl_info["text"] = "Player turn 1:  O"
    turn = "p1"
    for num in range(9):
        btn_list[num]["name"].config(bg="#fff", text=str(), state="normal")


def check_winner():
    if map[0][0] == map[1][0] == map[2][0] and map[0][0] != "-":
        if map[0][0] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif map[0][1] == map[1][1] == map[2][1] and map[0][1] != "-":
        if map[0][1] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif map[0][2] == map[1][2] == map[2][2] and map[0][2] != "-":
        if map[0][2] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif map[0][0] == map[1][1] == map[2][2] and map[0][0] != "-":
        if map[0][0] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif map[0][2] == map[1][1] == map[2][0] and map[0][2] != "-":
        if map[0][2] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif len(set(map[0])) == 1 and map[0][0] != "-":
        if map[0][0] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif len(set(map[1])) == 1 and map[1][0] != "-":
        if map[1][0] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif len(set(map[2])) == 1 and map[2][0] != "-":
        if map[2][0] == "O":
            message = "player 1 is winner."
        else:
            message = "player 2 is winner."
    elif "-" not in map[0] and "-" not in map[1] and "-" not in map[2]:
        message = "The game has no winner."
    else:
        return
    messagebox.showinfo(title="winner", message=message)
    reset_game()


turn = "p1"


def play(list_index, i, j):
    global turn, map
    if turn == "p1":
        text = "O"
        lbl_info["text"] = "Player turn 2:  X"
        bg = "#000FFF"
        turn = "p2"
    else:
        text = "X"
        lbl_info["text"] = "Player turn 1:  O"
        bg = "#FF0000"
        turn = "p1"

    btn_list[list_index]["name"].config(bg=bg, text=text, state="disable")
    map[i][j] = text
    check_winner()


heading_image = tk.PhotoImage(file="image/icon_heading.png").subsample(4, 4)
lbl_heading = tk.Label(
    root,
    text="  tic tac toe Game",
    compound="left",
    image=heading_image,
    font="arial 20 bold",
    bg="#000",
    fg="#8EB815",
).place(x=0, y=0, width=500, height=80)

lbl_info = tk.Label(
    root,
    text="Player turn 1:  O",
    font="arial 15 bold",
    relief="solid",
)

game = tk.Frame(
    root,
    bd=3,
    relief="solid",
)

for num, btn_dict in enumerate(btn_list):
    btn_dict["name"] = tk.Button(
        game,
        width=4,
        bd=3,
        font="arial 30 bold",
        relief="solid",
        command=btn_dict["function"],
    )
    btn_dict["name"].grid(row=(num // 3), column=(num % 3))


lbl_info.place(x=155, y=100, width=200)
game.place(x=85, y=170, width=330, height=255)


root.mainloop()
