from tkinter import *
from datetime import datetime

def start_drag(event):
    root.x = event.x
    root.y = event.y

def do_drag(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f"+{x}+{y}")

def add_letter_spacing(text, spacing=1):
    return (" " * spacing).join(text)

def update():
    time = datetime.now().strftime("- %H:%M -")
    date = datetime.now().strftime("%d %B, %Y.").upper()
    timelbl.config(text=time)
    datelbl.config(text=date)
    root.after(1000, update)

def lower_window(event):
    root.lower()

root = Tk()

window_width = 700
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = ((screen_width // 2) - (window_width // 2)) + 280
y_position = 30

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.resizable(False, False)
root.config(bg="#000")
root.overrideredirect(1)
root.wm_attributes("-transparentcolor", "#000")
# root.wm_attributes("-topmost", True)

day = datetime.now().strftime("%A").upper()
spaced_day = add_letter_spacing(day, spacing=1)
date = datetime.now().strftime("%d %B, %Y.").upper()
time = datetime.now().strftime("- %H:%M -")

daylbl = Label(root, text=spaced_day, background="#000", fg="#eeeeee", font=("Anurati", 50))
daylbl.pack()

datelbl = Label(root, text=date, background="#000", fg="#eeeeee", font=("Tw Cen MT", 15))
datelbl.pack()

timelbl = Label(root, text=time, background="#000", fg="#eeeeee", font=("Tw Cen MT", 15))
timelbl.pack(pady=10)

root.bind("<Button-1>", start_drag)
root.bind("<B1-Motion>", do_drag)

update()
root.bind('<FocusIn>', lower_window)
root.mainloop()
