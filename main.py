from tkinter import *
import webbrowser

jscode = ""
pycode = ""
status_string = "Status: Waiting for connection"  # default
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" # path to chrome on windows; modify for linux

def opencodeorg():
    webbrowser.get(chrome_path).open_new("code.org")  # link to custom project for drone

window = Tk()
# no geometry for dynamic resizing to fit contents
window.title("jstopy_pyparrot")
window.resizable(width=False, height=False)
jslabel = Label(window, text="JavaScript from code.org (click here to open)", fg="blue")

jslabel.bind("<Button-1>", lambda e: opencodeorg())

pylabel = Label(window, text="Converted Python output")  # demonstrative code output
jswindow = Text(window, width=80, height=48)
pywindow = Text(window, width=80, height=48, state=DISABLED)

# def connect():

def convert():
    jscode = jswindow.get("1.0", END)
    pycode = jscode
    pywindow.config(state=NORMAL)
    pywindow.delete("1.0", END)
    pywindow.insert(END, jscode)
    pywindow.config(state=DISABLED)

# def load():

inputframe = Frame(window)
status = Label(inputframe, text=status_string, bg="red", fg="white", width=50) # default status
droneconnect = Button(inputframe, text="Connect drone to pyparrot")  # command=connect
pydisplay = Button(inputframe, text="Convert->", command=convert)
pyload = Button(inputframe,text="Load code into pyparrot")  # command=load

jslabel.grid(row=0, column=0)
pylabel.grid(row=0, column=1)
jswindow.grid(row=1, column=0)
pywindow.grid(row=1, column=1)
inputframe.grid(row=2, column=0, columnspan=2)

droneconnect.grid(row=0, column=0, padx=5)
pydisplay.grid(row=0, column=1, padx=5)
pyload.grid(row=0, column=2, padx=5)
status.grid(row=1, column=0, columnspan=3, pady=5)



window.mainloop()