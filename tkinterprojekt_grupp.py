#importerar moduler
from tkinter import * 
import random

#Fönstret/GUIen
window = Tk()
window.title("Först till 50 - Tärningsspel")
window.geometry("200x400")

#Knappar och ettiketer
player1_label = Label(window, text="Spelare 1: 0", font=("Helvetica", 16))
player1_label.pack()

player2_label = Label(window, text="Spelare 2: 0", font=("Helvetica", 16))
player2_label.pack()

round_label = Label(window, text="Rundpoäng: 0", font=("Helvetica", 14))
round_label.pack()

dice_label = Label(window, text="Tärningskast: -", font=("Helvetica", 14))
dice_label.pack()

status_label = Label(window, text="Spelare 1s tur", font=("Helvetica", 14, "bold"))
status_label.pack(pady=10)

roll_button = Button(window, text="Kasta Tärning", font=("Helvetica", 12), bg="lightblue")
roll_button.pack(pady=5)

hold_button = Button(window, text="Spara Poäng", font=("Helvetica", 12), bg="lightgreen")
hold_button.pack(pady=5)

chaos_button = Button(window, text="CHAOS ROLL", font=("Helvetica", 12, "bold"), bg="#8B0000", fg="white")
chaos_button.pack(pady=5)

restart_button = Button(window, text="Starta om", font=("Helvetica", 12), bg="orange")
restart_button.pack(pady=10)



window.mainloop()





