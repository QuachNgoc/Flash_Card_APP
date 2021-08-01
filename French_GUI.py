from tkinter import *
from random import choice
import pandas as pd
BACKGROUND_COLOR = "#B5EAEA"


class Fr_GUI:
    def __init__(self, master) -> object:
        self.master = master
        master.title("Flash Cards learn French Vocabulary")
        master.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.current_card = {}
        self.to_learn = {}
        try:
            self.data_file = pd.read_csv("./data/French_words_to_learn.csv")
        except FileNotFoundError:
            self.original_data = pd.read_csv("./data/french_words.csv")
            self.to_learn = self.original_data.to_dict(orient="records")
        else:
            self.to_learn = self.data_file.to_dict(orient="records")

        self.flip_timer = master.after(3000, func= self.flip_card)

        # Canvas
        # Card Front canvas

        self.card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front_img = PhotoImage(file="./images/card_front.png")
        self.card_back_img = PhotoImage(file="./images/card_back.png")
        self.front_card = self.card.create_image(400, 263, image= self.card_front_img)

        self.card_title = self.card.create_text(400, 150, text="Ready!", font=("Ariel", 40, "italic"), fill="black")
        self.card_word = self.card.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
        self.card.grid(column=0, row=0, columnspan=2)

        # Label

        self.know_it = Label(text="I know it!", font=("Ariel", 20, "bold"), bg=BACKGROUND_COLOR)
        self.know_it.grid(column=0, row=3)

        self.dont_know = Label(text="Don't know", font=("Ariel", 20, "bold"), bg=BACKGROUND_COLOR)
        self.dont_know.grid(column=1, row=3)

        # Button
        self.right_button_image = PhotoImage(file="./images/right.png")
        self.right_button = Button(image=self.right_button_image, highlightthickness=0, command= self.next_card)
        self.right_button.grid(column=0, row=1)

        self.wrong_button_image = PhotoImage(file="./images/wrong.png")
        self.wrong_button = Button(image=self.wrong_button_image, highlightthickness=0, command= self.is_known)
        self.wrong_button.grid(column=1, row=1)

        # --------------------Next Front Card---------------#

    def next_card(self):
        self.master.after_cancel(self.flip_timer)

        self.current_card = choice(self.to_learn)
        self.card.itemconfig(self.card_title, text="French", fill="black")
        self.card.itemconfig(self.card_word, text= self.current_card["French"], fill="black")
        self.card.itemconfig(self.front_card, image=self.card_front_img)

        self.flip_timer = self.master.after(3000, func=self.flip_card)

    def flip_card(self):
        self.card.itemconfig(self.front_card, image=self.card_back_img)
        self.card.itemconfig(self.card_title, text="English", fill="white")
        self.card.itemconfig(self.card_word, text=self.current_card["English"], fill="white")

    def is_known(self):
        self.to_learn.remove(self.current_card)
        new_data = pd.DataFrame(self.to_learn)
        new_data.to_csv("data/french_words_to_learn.csv", index=False)
        self.next_card()