import tkinter as tk
from datetime import datetime
from math import sin, cos, radians

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    hour, minute, second = current_time.split(":")

    hour = int(hour) % 12
    minute = int(minute)
    second = int(second)

    # Draw clock face
    canvas.create_oval(50, 50, 350, 350, fill="white")
    canvas.create_oval(70, 70, 330, 330, fill="light grey")

    # Draw clock hands
    second_hand = canvas.create_line(200, 200, 200 + 150 * sin(radians(second * 6)),200 - 150 * cos(radians(second * 6)),width=1, fill="red")
    minute_hand = canvas.create_line(200, 200, 200 + 130 * sin(radians(minute * 6)),200 - 130 * cos(radians(minute * 6)), width=3, fill="black")
    hour_hand = canvas.create_line(200, 200, 200 + 100 * sin(radians((hour * 30) + (minute/2))),200 - 100 * cos(radians((hour * 30) + (minute/2))),width=5, fill="black")

    canvas.after(1000, update_time)

update_time()
root.mainloop()
