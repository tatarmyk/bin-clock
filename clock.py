import tkinter as tk
import time

def update_clock():
    # Get the current time
    now = time.localtime()
    seconds_since_midnight = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec

    # Calculate the total seconds in a day
    total_seconds_in_day = 24 * 60 * 60

    # Calculate the current time in bhours and binutes
    current_bhour = (seconds_since_midnight / total_seconds_in_day) * 32
    current_binute = (current_bhour % 1) * 32
    current_becond = (current_binute % 1) * 64

    # Format the current time as a string
    current_time = f"{int(current_bhour):02}:{int(current_binute):02}:{int(current_becond):02}"

    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("Clock")

# Make the window stay on top
root.attributes('-topmost', 1)

clock_label = tk.Label(root, font=("Arial", 24), bg="#eef5db", fg="#39375b")
clock_label.pack(padx=20, pady=20)

update_clock()

root.mainloop()