from tkinter import *
import random

# Skapa fönster
root = Tk()
root.title("Först till 50 - Tärningsspel")

# --- Widgets ---
player1_label = Label(root, text="Spelare 1: 0", font=("Helvetica", 16))
player1_label.pack()

player2_label = Label(root, text="Spelare 2: 0", font=("Helvetica", 16))
player2_label.pack()

round_label = Label(root, text="Rundpoäng: 0", font=("Helvetica", 14))
round_label.pack()

dice_label = Label(root, text="Tärningskast: -", font=("Helvetica", 14))
dice_label.pack()

status_label = Label(root, text="Spelare 1s tur", font=("Helvetica", 14, "bold"))
status_label.pack(pady=10)

roll_button = Button(root, text="Kasta Tärning", font=("Helvetica", 12), bg="lightblue")
roll_button.pack(pady=5)

hold_button = Button(root, text="Spara Poäng", font=("Helvetica", 12), bg="lightgreen")
hold_button.pack(pady=5)

chaos_button = Button(root, text="CHAOS ROLL", font=("Helvetica", 12, "bold"), bg="#8B0000", fg="white")
chaos_button.pack(pady=5)

restart_button = Button(root, text="Starta om", font=("Helvetica", 12), bg="orange")
restart_button.pack(pady=10)

# --- Globala variabler ---
player_scores = [0, 0]
round_score = 0
current_player = 0

# --- Spellogik ---
def roll_dice():
    global round_score, current_player
    roll = random.randint(1, 6)
    dice_label.config(text=f"Tärningskast: {roll}")
    
    if roll == 1:
        round_score = 0
        update_round_score()
        switch_player()
    else:
        round_score += roll
        update_round_score()
        update_scores()

def hold():
    global player_scores, round_score, current_player
    player_scores[current_player] += round_score
    round_score = 0
    update_scores()

    if player_scores[current_player] >= 50:
        status_label.config(text=f"Spelare {current_player+1} vinner!")
        disable_buttons()
    else:
        switch_player()

def chaos_roll():
    global player_scores, round_score, current_player
    roll = random.choices([1, 2, 3, 4, 5, 6], weights=[3, 1, 1, 1, 1, 1])[0]
    dice_label.config(text=f"CHAOS ROLL: {roll}")

    if roll == 1:
        player_scores[current_player] = 0
        round_score = 0
        update_scores()
        status_label.config(text=f"Spelare {current_player+1} slog en etta! Alla poäng förlorade!")
        switch_player()
    else:
        round_score += roll * 2
        update_round_score()
        update_scores()

def switch_player():
    global current_player
    current_player = 1 - current_player
    update_scores()

def update_scores():
    player1_label.config(text=f"Spelare 1: {player_scores[0]}")
    player2_label.config(text=f"Spelare 2: {player_scores[1]}")

    if current_player == 0:
        player1_label.config(bg="yellow")
        player2_label.config(bg=root["bg"])
    else:
        player1_label.config(bg=root["bg"])
        player2_label.config(bg="yellow")

    update_round_score()
    status_label.config(text=f"Spelare {current_player+1}s tur")

def update_round_score():
    round_label.config(text=f"Rundpoäng: {round_score}")

def restart_game():
    global player_scores, round_score, current_player
    player_scores = [0, 0]
    round_score = 0
    current_player = 0
    enable_buttons()
    update_scores()
    dice_label.config(text="Tärningskast: -")

def disable_buttons():
    roll_button.config(state=DISABLED)
    hold_button.config(state=DISABLED)
    chaos_button.config(state=DISABLED)

def enable_buttons():
    roll_button.config(state=NORMAL)
    hold_button.config(state=NORMAL)
    chaos_button.config(state=NORMAL)

# --- Koppla knappar till funktioner ---
roll_button.config(command=roll_dice)
hold_button.config(command=hold)
chaos_button.config(command=chaos_roll)
restart_button.config(command=restart_game)

# Starta spelet med korrekt highlight
update_scores()
root.mainloop()
