# this will draw a Parabola
import math
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter


# functions
# create parabola
def parabola(page, size):
    for x in range(size):
        y = x * x / size
        plot(page, x, y)
        plot(page, -x, y)


# draw circle
def circle(page, radius, g, h):
    for x in range(g, g + radius):
        y = h + (math.sqrt(radius ** 2 - ((x - g) ** 2)))
        plot(page, x, y)
        plot(page, x, 2 * h - y)
        plot(page, 2 * g - x, y)
        plot(page, 2 * g - x, 2 * h - y)


# draw grid on GUI
def draw_axis(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="white")
    page.create_line(0, y_origin, 0, -y_origin, fill="white")


# draw parabola
def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")

# GUI generation
mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

# Draws UI grid
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axis(canvas)

# Draw parabolas
parabola(canvas, 100)
parabola(canvas, 200)

# Draw circles
circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100)
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)


# render gui
mainWindow.mainloop()