from tkinter import *
from GUI import Eng_GUI
from French_GUI import Fr_GUI

BACKGROUND_COLOR = "#B1DDC6"


def ENG_GUI():
    gui=Eng_GUI(window)

def FRENCH_GUI():
    gui = Fr_GUI(window)

# --------------------SET UP GUI-------------------#

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashing")
label=Label(text="Let's Learn: ", font=("Ariel", 20, "bold"), bg=BACKGROUND_COLOR)

en_button = Button(text="English", highlightthickness=0, command=ENG_GUI)
en_button.grid(column=0, row=1)
label.grid(column=0, row=0, columnspan=2)

fr_button = Button(text="French", highlightthickness=0, command=FRENCH_GUI)
fr_button.grid(column=1, row=1)

window.mainloop()



