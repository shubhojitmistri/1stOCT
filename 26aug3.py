import tkinter as tk

root = tk.Tk()
root.title("3D Gradient Squares")

canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

square_size = 40
rows, cols = 10, 10
c = 0

for i in range(rows):
    for j in range(cols):
        x1 = j * square_size
        y1 = i * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size

        # Alternate between Blue->Green and Green->Blue
        if c % 2 == 0:
            start_color, end_color = (0, 0, 255), (0, 255, 0)  # blue to green
        else:
            start_color, end_color = (0, 255, 0), (0, 0, 255)  # green to blue

        # Draw gradient effect
        steps = 20
        for k in range(steps):
            r = int(start_color[0] + (end_color[0] - start_color[0]) * (k / steps))
            g = int(start_color[1] + (end_color[1] - start_color[1]) * (k / steps))
            b = int(start_color[2] + (end_color[2] - start_color[2]) * (k / steps))

            color = f'#{r:02x}{g:02x}{b:02x}'
            y = y1 + (square_size * k / steps)
            canvas.create_rectangle(x1, y, x2, y + square_size / steps, fill=color, outline=color)

        c += 1

root.mainloop()
