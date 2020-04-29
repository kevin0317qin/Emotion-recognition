import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from Command import cmd1
from GetRecord import get_record
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk



myWindow = tk.Tk()

myWindow.title('Emotional recognition')

width = 800
height = 560

screenwidth = myWindow.winfo_screenwidth()
screenheight = myWindow.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
myWindow.geometry(alignstr)

myWindow.resizable(width=False, height=True)

col_count, row_count = myWindow.grid_size()

for col in range(col_count):
    myWindow.grid_columnconfigure(col, minsize=5)

for row in range(row_count):
    myWindow.grid_rowconfigure(row, minsize=15)


photo_start=tk.PhotoImage(file="start.gif")

label=tk.Label(myWindow,image=photo_start)

label.grid(row=0, column=0, sticky=tk.NW)

photo_happy=tk.PhotoImage(file="Happy.gif")

photo_sad=tk.PhotoImage(file="Sad.gif")

photo_angry=tk.PhotoImage(file="Angry.gif")

photo_surprise=tk.PhotoImage(file="Surprise.gif")

emotions=tk.StringVar()
emo = tk.Label(myWindow,
               textvariable=emotions,
               font=('Arial', 12), width=20, height=2)

emo.grid(row=0, column=6)
var = tk.StringVar()
l = tk.Label(myWindow,
             textvariable=var,
             bg='white', font=('Arial', 12), width=20, height=2)

l.grid(row=1, column=6)
path = tk.StringVar()

var2 = tk.StringVar() #information

var.set('Recording in 5 seconds')

def change_Image(emotion):
    label.config(image=emotion)


on_hit = False
def get_audio():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('End of recording')


        get_record("output.wav")

    else:
        on_hit = False
        var.set('Wait recording')



def cmd():
    global on_hit
    if on_hit == True:

        emotion = cmd1()
        if emotion == "Angry":
            emotions.set("You sound very angry!")
            change_Image(photo_angry)
        elif emotion == "Happy":
            emotions.set("You sound very happy!")
            change_Image(photo_happy)
            # label.config(image=photo_happy)
        elif emotion == "Sad":
            emotions.set("You sound very sad!")
            change_Image(photo_sad)
            # label.config(image=photo_sad)
        elif emotion == "Surprise":
            emotions.set("You sound very surprise!")
            change_Image(photo_surprise)
            # label.config(image=photo_surprise)
    else:
        var2.set("You should recording firstly!")


b = tk.Button(myWindow,
              text='Recroding',
              width=8, height=2,
              bg = "blue",
              activebackground = "white",
              command=get_audio)
b.grid(row=2, column=6)
# b.pack(side=tk.RIGHT)
c = tk.Button(myWindow,
              text="Testing",
              width=8, heigh=2,
              bg = "blue",
              activebackground = "white",
              command=cmd)
c.grid(row=3, column=6)
# c.pack(side=tk.RIGHT)
l1 = tk.Label(myWindow,
              textvariable=var2,
              bg='white', font=('Arial', 12), width=30, height=2)
# l1.pack(side=tk.RIGHT)
l1.grid(row=4, column=6)




myWindow.mainloop()