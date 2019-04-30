import math
import gettext
from tkinter import *
import os.path

#datapath = os.path.dirname(sys.argv[0])
#gettext.install('messages', datapath)
#gettext.bindtextdomain('main_app', localedir=None)
#gettext.gettext('main_app')

bindir=os.path.realpath(sys.argv[0])
for localedir in bindir, None, ".":
    localefile=gettext.find('main_app',localedir)
    if localefile: 
        break
gettext.install('main_app','./ru/LC_MESSAGES')

root = Tk()#for quit_function

prev_x = None
prev_y = None
old_i = -1

def cross(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
    v1=(bx2-bx1)*(ay1-by1)-(by2-by1)*(ax1-bx1)
    v2=(bx2-bx1)*(ay2-by1)-(by2-by1)*(ax2-bx1)
    v3=(ax2-ax1)*(by1-ay1)-(ay2-ay1)*(bx1-ax1)
    v4=(ax2-ax1)*(by2-ay1)-(ay2-ay1)*(bx2-ax1)
    if((v1*v2<0) and (v3*v4<0)):
       return True
    else:
       return False

def find_point(x1,y1,x2,y2,x3,y3,x4,y4):
    coord=[0]*3
    if(x4!=x3):
        coord[0]=-((x1*y2-x2*y1)*(x4-x3)-(x3*y4-x4*y3)*(x2-x1))/((y1-y2)*(x4-x3)-(y3-y4)*(x2-x1))
        coord[1]=((y4-y3)*coord[0]-(x3*y4-x4*y3))/(x4-x3)
    else:
        coord[1]=-((y1*x2-y2*x1)*(y4-y3)-(y3*x4-y4*x3)*(y2-y1))/((x1-x2)*(y4-y3)-(x3-x4)*(y2-y1))
        coord[0]=((x4-x3)*coord[0]-(y3*x4-y4*x3))/(y4-y3)
    coord[2]=math.sqrt((x1-coord[0])**2+(y1-coord[1])**2)
    return coord

def find_mir(Cx,Cy,Ax,Ay,A1x,A1y,A2x,A2y):
    coord=[0]*2
    Dx=A2x-A1x
    Dy=A2y-A1y
    if(Dy==0):
        Bx=0
        By=1
    else:
        Bx=1
        By=-Dx/Dy
    f=(Ay*Bx-Cy*Bx+By*(Cx-Ax))/(Dy*Bx-By*Dx)
    coord[0]=Cx+2*f*Dx
    coord[1]=Cy+2*f*Dy
    return coord

class Room:
    Number_of_walls = 0
    Coordinates = []

ourRoom = Room()

class Laser:
    Position_x  = 0
    Position_y  = 0
    Direction_x = 0
    Direction_y = 0

ourLaser = Laser()

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
        self.canvasRoom = Canvas(self, width=400, height=700, bg='#FFFFFF')
        self.canvasRoom.pack()
        self.canvasRoom.grid(columnspan=1, sticky=W+N+E)
        self.canvasRoom.bind("<Motion>", self.mousemove)
        self.buttonFrame = Frame(self)
        self.buttonFrame.grid(row=1, column=0, sticky=W)
        self.buttonBuildRoom = Button(self.buttonFrame, text=_("Build Room"), command=self.buildroom)
        self.buttonBuildRoom.grid(row=1, column=0, sticky=W)
        self.buttonBuildLaser = Button(self.buttonFrame, text=_("Place Laser"), command=self.placelaser)
        self.buttonBuildLaser.grid(row=1, column=1, sticky=W)
        self.buttonNextReflection = Button(self.buttonFrame, text=_("Next Reflection"), command=self.nextreflection)
        self.buttonNextReflection.grid(row=1, column=2, sticky=W)
        self.buttonQuit = Button(self.buttonFrame, text=_("Quit"), command=self.quit_function)
        self.buttonQuit.grid(row=1, column=3, sticky=W)
        self.XCoordLabel = Label(self.buttonFrame, text = 'X')
        self.XCoordLabel.grid(row=1, column=4)
        self.YCoordLabel = Label(self.buttonFrame, text = 'Y')
        self.YCoordLabel.grid(row=1, column=5)

    def quit_function(ev):
        global root
        root.destroy()
		
    def mousemove(self, event):
        self.XCoordLabel.config(text = event.x)
        self.YCoordLabel.config(text = event.y)

    def buildroom(self):
        self.canvasRoom.bind("<1>", self.clickroom)

    def clickroom(self, event):
        global prev_x, prev_y, ourRoom
        x = event.x
        y = event.y

        self.canvasRoom.create_oval(x-1,y-1,x+1,y+1,width=1)
        ourRoom.Coordinates.append(x)
        ourRoom.Coordinates.append(y)
        ourRoom.Number_of_walls += 1
        
        if prev_x:
            self.canvasRoom.create_line(x,y,prev_x,prev_y,width=1)
     
        prev_x = x
        prev_y = y

    def placelaser(self):
        self.canvasRoom.create_line(ourRoom.Coordinates[0],ourRoom.Coordinates[1],ourRoom.Coordinates[len(ourRoom.Coordinates)-2],ourRoom.Coordinates[len(ourRoom.Coordinates)-1])
        self.canvasRoom.bind("<1>", self.clicklaser)

    def clicklaser(self, event):
        global ourLaser
        x = event.x
        y = event.y
        ourLaser.Position_x = x
        ourLaser.Position_y = y
        ourLaser.Direction_x = x
        ourLaser.Direction_y = y+10
        
        self.canvasRoom.create_oval(x-1,y-1,x+1,y+1,width=2, fill = "red", outline = "red")

    def nextreflection(self):
        global ourRoom, ourLaser
        self.canvasRoom.bind("<1>", self.Laser_step(ourRoom, ourLaser))
        
    def Laser_step(self, r, l1):
        global ourLaser, old_i
        l2=Laser()
        dl1x = l1.Direction_x
        dl1y = l1.Direction_y
        pl1x = l1.Position_x
        pl1y = l1.Position_y

        dl2x = l2.Direction_x
        dl2y = l2.Direction_y
        pl2x = l2.Position_x
        pl2y = l2.Position_y   
        
        mas1=[0]*3
        mas2=[0]*2
        dl2x = pl1x + (dl1x - pl1x)*20000/(math.sqrt((dl1x - pl1x)**2+(dl1y-pl1y)**2))
        dl2y = pl1y+(dl1y-pl1y)*20000/(math.sqrt((dl1x-pl1x)**2+(dl1y-pl1y)**2))
        #print (int(dl2x), int(dl2y), int(pl2x), int(pl2y))
        dl1x = dl2x 
        dl1y = dl2y
        mas1[0]=pl1x
        mas1[1]=pl1y
        if(cross(pl1x,pl1y,dl1x,dl1y,0,0,0,9900)): 
            mas1=find_point(pl1x,pl1y,dl1x,dl1y,0,0,0,9900)
            #print("1")
        if(cross(pl1x,pl1y,dl1x,dl1y,0,0,9900,0)):
            mas1=find_point(pl1x,pl1y,dl1x,dl1y,0,0,9900,0)
            #print("2")
        if(cross(pl1x,pl1y,dl1x,dl1y,9900,9900,9900,0)):
            mas1=find_point(pl1x,pl1y,dl1x,dl1y,9900,9900,9900,0)
            #print("3")
        if(cross(pl1x,pl1y,dl1x,dl1y,9900,9900,0,9900)):
            mas1=find_point(pl1x,pl1y,dl1x,dl1y,9900,9900,0,9900)
            #print("4")
        dl1x = mas1[0]
        dl1y = mas1[1]
        pl2x = mas1[0]
        pl2y = mas1[1]
        dl2x = mas1[0]
        dl2y = mas1[1]
        #print (int(dl1x), int(dl1y), int(pl1x), int(pl1y))
        #print (int(dl2x), int(dl2y), int(pl2x), int(pl2y))
        rmin=20000
        new_i=-1
        for i in range (r.Number_of_walls):
            if(cross(pl1x,pl1y,dl1x,dl1y,r.Coordinates[2*i],r.Coordinates[(2*i) + 1],r.Coordinates[int((2*i+2)%(2*r.Number_of_walls)) ],r.Coordinates[int((2*i + 3)%(2*r.Number_of_walls)) ])):
                mas1=find_point(pl1x,pl1y,dl1x,dl1y,r.Coordinates[2*i],r.Coordinates[(2*i) + 1],r.Coordinates[int((2*i+2)%(2*r.Number_of_walls)) ],r.Coordinates[int((2*i + 3)%(2*r.Number_of_walls))])
                if((mas1[2]<rmin)and(i!=old_i)):
                    #print("i=",i)
                    new_i=i
                    rmin = mas1[2]
                    pl2x = mas1[0]
                    pl2y = mas1[1]
                    mas2=find_mir(pl1x,pl1y,mas1[0],mas1[1],r.Coordinates[(2*i)],r.Coordinates[(2*i) + 1],r.Coordinates[int((2*i+2)%(2*r.Number_of_walls)) ],r.Coordinates[int((2*i + 3)%(2*r.Number_of_walls))])
                    dl2x=mas2[0]
                    dl2y=mas2[1]
        self.canvasRoom.create_line(ourLaser.Position_x,ourLaser.Position_y,int(pl2x) ,int(pl2y) ,fill="red", width=2)
        old_i=new_i
        ourLaser.Position_x  = (pl2x) 
        ourLaser.Position_y  = (pl2y) 
        ourLaser.Direction_x = (dl2x)
        ourLaser.Direction_y = (dl2y)
        print (int(dl2x), int(dl2y), int(pl2x), int(pl2y))

app = MirrorRoomApp(Title="Mirror Room")
app.mainloop()
