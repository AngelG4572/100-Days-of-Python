from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# ---------------------------- PANDAS ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
except pandas.errors.EmptyDataError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    word_dict = data.to_dict(orient="records")

# ---------------------------- COMMANDS ------------------------------- #
new_word = ''
flip_timer = None


def change_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(word_dict)
    canvas.itemconfig(flashcard, image=card_front_png)
    new_french_word = new_word["French"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(vocab_word, text=new_french_word, fill="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    new_english_word = new_word['English']
    canvas.itemconfig(flashcard, image=card_back_png)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(vocab_word, text=new_english_word, fill="white")


def knew_word():
    if new_word in word_dict:
        word_dict.remove(new_word)

    change_word()


def wrong_word():
    change_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_png = PhotoImage(file="images/card_front.png")
card_back_png = PhotoImage(file="images/card_back.png")
flashcard = canvas.create_image(400, 263, image=card_front_png)
title = canvas.create_text(400, 150, text="", font=LANG_FONT)
vocab_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

right_button_image = PhotoImage(file="images/right.png")
button = Button(image=right_button_image, highlightthickness=0, command=knew_word)
button.grid(row=1, column=1)
wrong_button_image = PhotoImage(file="images/wrong.png")
button = Button(image=wrong_button_image, highlightthickness=0, command=wrong_word)
button.grid(row=1, column=0)

flip_timer = window.after(3000, flip_card)
change_word()
window.mainloop()

word_df = pandas.DataFrame(word_dict)
word_df.to_csv("data/words_to_learn.csv", index=False)
