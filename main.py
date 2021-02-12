from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKMARK = "✔"
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarks.config(text="")
    tomator.config(text="Pro")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if(REPS % 8 == 0 and REPS != 0):
        count_down(long_break)
        tomator.config(text="Long break")
    else:
        if(REPS % 2 == 0):
            count_down(work)
            tomator.config(text="Grind the Grinder")
        else:
            checkmarks.config(text=checkmarks["text"] + CHECKMARK)
            count_down(short_break)
            tomator.config(text="Shorty break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
    global REPS
    if(count == 0):
        REPS+=1
        start_timer()
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if (count != 0):
        global timer
        timer = window.after(1000, count_down, count-1)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=10, pady=5, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(bg=YELLOW,width=200, height=224, highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00", font=(FONT_NAME, 35, "bold"), fill=YELLOW)

canvas.grid(column=1, row=1)

# Labels

title = Label(text="🧘🏽 Zen Timer ")
title.config(bg=YELLOW,fg=GREEN, font=(FONT_NAME, 36, "bold"))
title.grid(column=1, row=0)

tomator = Label(text="Pro+")
tomator.config(bg=YELLOW,fg=RED, font=(FONT_NAME, 36, "bold"))
tomator.grid(column=1, row=4)

checkmarks = Label(text="")
checkmarks.config(bg=YELLOW,fg=GREEN, font=(FONT_NAME, 24, "bold"))
checkmarks.grid(column=1, row=3)



# Buttons
def start():
    count_down(WORK_MIN*60)

start = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 24), command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 24), command=reset_timer)
reset.grid(column=2, row=3)



window.mainloop()