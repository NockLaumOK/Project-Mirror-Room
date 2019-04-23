from tkinter import *

class MirrorRoomApp(Frame):
    '''Base framed application class'''
    def __init__(self, master=None, Title="Application"):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title(Title)
        self.grid(sticky=N+E+S+W)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.create()

    def create(self):
        '''Create all the widgets'''
        self.canvasRoom = Canvas(self, width=600, height=500, bg='#FFFFFF')
        self.canvasRoom.grid(columnspan=1, sticky=W+N+E)
        self.canvasRoom.bind("<Motion>", self.mousemove)
        self.buttonFrame = Frame(self)
        self.buttonFrame.grid(row=1, column=0, sticky=W)
        self.buttonBuildRoom = Button(self.buttonFrame, text='Build Room')
        self.buttonBuildRoom.grid(row=1, column=0, sticky=W)
        self.buttonBuildLaser = Button(self.buttonFrame, text='Place Laser')
        self.buttonBuildLaser.grid(row=1, column=1, sticky=W)
        self.buttonNextReflection = Button(self.buttonFrame, text='Next Reflection')
        self.buttonNextReflection.grid(row=1, column=2, sticky=W)
        self.buttonQuit = Button(self.buttonFrame, text='Quit', command=self.quit)
        self.buttonQuit.grid(row=1, column=3, sticky=W)
        self.XCoordLabel = Label(self.buttonFrame, text = 'X')
        self.XCoordLabel.grid(row=1, column=4)
        self.YCoordLabel = Label(self.buttonFrame, text = 'Y')
        self.YCoordLabel.grid(row=1, column=5)

		
    def mousemove(self, event):
        self.XCoordLabel.config(text = event.x)
        self.YCoordLabel.config(text = event.y)

app = MirrorRoomApp(Title="Mirror Room")
app.mainloop()