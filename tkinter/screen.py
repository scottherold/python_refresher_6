# advanced GUI (this is so similar to CSS)
import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8 # sets padding for the GUI container

# Header
label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

# configuration
# width/column/height are determined by the widgets placed within them
# columns
# the weight property is used when the window is resized: higher weight
# means that the widget will resize (faster)/larger relative to widgets
# with lower weight values (these will disappear quicker when the 
# window is made smaller)
mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

# rows
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

# widget boxes
# window for list of files
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
# inserts files into the window
for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)

# scrollbar for file list
# command is how you link events in the GUI to actions in the code
# this is like JS event listeners
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL,
             command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
# attaches command to the scrollbar object
fileList['yscrollcommand'] = listScroll.set

# frame for the radio buttons
# LabelFrame draws a border around its contents
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

# radio button values
rbValue = tkinter.IntVar()
rbValue.set(1) # sets default option

# actual radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1,
         variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2,
         variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3,
         variable=rbValue)
# added to GUI
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget for displaying results for the file selected
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
# selected result display area
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')
# time spinners (multiple ways of producing output text/options)
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
# formatting
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
# frame padding
timeFrame['padx'] = 36

# frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# date labels
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
# formatting
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
# the values displays anything listed within the tuple
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", 
            "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
# fotmatting
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# buttons
okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel",
               command=mainWindow.destroy) # .destroy exits the window
# formatting
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

# GUI render
mainWindow.mainloop()

# .get() will return the data!
print(rbValue.get())