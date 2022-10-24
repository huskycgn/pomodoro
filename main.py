from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer, timer_text, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    checkmarks.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    global reps, timer_label, checkmarks
    reps += 1
    # normal work!
    if reps % 2 != 0 and reps != 8:
        timer_label.config(fg=GREEN, text='Work')
        count_down(work_sec)
        # 5-minute break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(fg=PINK, text='Break')
        # 20-minute break
    else:
        timer_label.config(fg=RED, text='Break')
        count_down(long_break_sec)

    if reps % 2 == 0:
        checkmarks.config(text='✅' * int((reps / 2)))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min:02d}:{count_sec:02d}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# window.after(1000, day_something, 'Hello')
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'normal'))
timer_label.grid(row=0, column=1)

button_start = Button(text='Start', highlightthickness=0, command=start_timer)
button_reset = Button(text='Reset', highlightthickness=0, command=reset_timer)
checkmarks = Label(text='', fg=GREEN, bg=YELLOW)
checkmarks.grid(row=3, column=1)

button_start.grid(row=2, column=0)
button_reset.grid(row=2, column=2)

window.mainloop()
