# Write a GUI program to create a simple calculator layout that looks
# like the screenshot.
#
# TRy to be as Pythonic as possible - it's ok if you end up writing
# repeated Button and Grid statements, but consider using lists and a
# for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to work out of to use
# minsize() to prevent your window from being shrunk so that the widgets
# vanish from view
#
# Hint: you may want to use the widgets .winfo_height() and
# .winfo_width() methods, in which case you should know they will not
# return the correct results unless the window has been forced to draw
# the widgets by calling its .update() method first.

import tkinter

# Calculator keys
keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('3', 1), ('2', 1), ('1', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)]]

# window config
mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

# number entry bar
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

# keypad UI
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

# display keys
row = 0
# iterate through each nested list
for keyRow in keys:
    col = 0
    # iterate through each touple within the list
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col,
            columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

# GUI render
mainWindow.update()
# prevents the window from getting smaller than the widgets
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding,
    result.winfo_height() + keyPad.winfo_height())
# prevents the window from being resized larger
mainWindow.maxsize(keyPad.winfo_width() + 50 + mainWindowPadding,
    result.winfo_height() + keyPad.winfo_height())
mainWindow.mainloop()