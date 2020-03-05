# like demo, but with grid instead of pack
# remember, with WSL you need to launch xming
import tkinter

# GUI development
mainWindow = tkinter.Tk()

mainWindow.title("Hello World")

# screen resolution
mainWindow.geometry('640x480+8+400')

# GUI design
label = tkinter.Label(mainWindow, text="Hello World")
# grid provides a layout based on row/column, instead of side
# orientation, which is used in pack
label.grid(row=0, column=0)

# frames can be used as containers for geometry objects (widget)
leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
# 'sticky' is the same as 'acnhor' from pack
rightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
# nested widgets created rows/columns within the parent
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure columns
# position
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

# appearance
leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)

# size
leftFrame.grid(sticky='ns') # n(orth) s(outh) = full height
# n(orth), e(ast), w(est) = full width, top alignment
rightFrame.grid(sticky='new')

# weight allows for nested widgets to change their size within their
# parent
rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

# passes control from console to tk (runs the program in the GUI)
mainWindow.mainloop()