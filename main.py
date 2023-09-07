import random
import tkinter as tk

global_setup = 5  # dimension of board


def simple_version():
    num25 = [i + 1 for i in range(25)]
    for i in range(5):
        for j in range(5):
            choosen = random.choice(num25)
            num25.remove(choosen)
            print(f'{choosen}', end='\t')
        print()


def generate_random_numbers():
    num25 = [i + 1 for i in range(global_setup * global_setup)]
    random.shuffle(num25)
    return [num25[i:i + global_setup] for i in range(0, global_setup * global_setup, global_setup)]


def update_board():
    global cell_label
    for i in range(5):
        for j in range(5):
            cell_label[i][j].config(text=board[i][j])


def new_game():
    global board
    board = generate_random_numbers()
    update_board()


def complex_version():
    window = tk.Tk()
    window.title("Random Number Game")

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20)

    board = generate_random_numbers()

    for i in range(global_setup):
        row_labels = []
        for j in range(global_setup):
            label = tk.Label(frame, text=board[i][j], width=5, height=2, relief=tk.RIDGE, padx=10, pady=10)
            label.grid(row=i, column=j)
            label.config(font=('Helvatical bold', 16))
            row_labels.append(label)
        cell_label.append(row_labels)

    new_game_button = tk.Button(window, text="New Game", command=new_game)
    new_game_button.pack(pady=0)
    window.mainloop()


if __name__ == '__main__':
    cell_label = []
    # simple_version()
    complex_version()
