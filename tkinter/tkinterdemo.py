# non-web GUI's (YAY!)
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# # runs a GUI test
# tkinter._test()

# GUI development
mainWindow = tkinter.Tk()

mainWindow.title("Hello World")

# screen resolution
# offsets (Where window appears on screen) represented by +/-
mainWindow.geometry('640x480+8+400')

# passes control from console to tk
mainWindow.mainloop()