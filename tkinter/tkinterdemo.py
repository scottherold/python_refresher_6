# non-web GUI's (YAY!)
# remember, with WSL you need to launch xming
import tkinter

# GUI development
mainWindow = tkinter.Tk()

mainWindow.title("Hello World")

# screen resolution
# offsets (Where window appears on screen) represented by +/-
mainWindow.geometry('640x480+8+400')

# GUI design
label = tkinter.Label(mainWindow, text="Hello World")
# side = orientation on the window
label.pack(side='top')

# frames can be used as containers for geometry objects (widget)
leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
# fill = the area that the widget will cover
# tkinter.Y and tkinter.X are both fill options
# fill is based on side (orientation); if orientation is left/right,
# the expand option must be used for X, and if orientation is top/bottom,
# the expand option must be used for Y
# canvas.pack(side='left', fill=tkinter.X, expand=True)

# widgets will share the same side in the order that they are packed
# to adjust this, you can pass the anchor option to .pack();
# Note that this position IS STILL based on the order with pack
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand='true')

button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

# passes control from console to tk (runs the program in the GUI)
mainWindow.mainloop()