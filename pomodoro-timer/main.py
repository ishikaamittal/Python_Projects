import math
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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="TIMER")
    tick.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        heading.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        heading.config(text="BREAK", fg=PINK)
    else:
        count_down(work_time)
        heading.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(900, count_down, count - 1)
    else:
        start_timer()
        tick_mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            tick_mark += "✔"
        tick.config(text=tick_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text="TIMER", fg=GREEN, font=("Courier", 30, "bold"), bg=YELLOW)
heading.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 22, "bold"))
canvas.grid(row=2, column=2)

start_button = Button(text="Start", width=10, command=start_timer)
start_button.grid(row=3, column=1)

tick = Label(text="", font=("Arial", 18, "bold"), bg=YELLOW, fg=GREEN)
tick.grid(row=3, column=2)

reset_button = Button(text="Reset", width=10, command=reset)
reset_button.grid(row=3, column=3)

window.mainloop()
