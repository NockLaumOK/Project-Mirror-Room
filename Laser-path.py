import math

#Класс комнаты
class Room:
    #[Переменная] Количество стен в комнате
    Number_of_walls = 0

    #[Переменная] Матрица координат вершин стен
    Nodes = [0] * Number_of_walls
    for i in range (Number_of_walls):
        Nodes[i] = [0] * 2
#Класс лазера
class Laser:
    #[Переменная] Положение лазера
    Position = [0] * 2

    #[Переменная] Направление вектора
    Direction = [0] * 2


def cross(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):#Проверка пересечения двух отрезков
   v1=(bx2-bx1)*(ay1-by1)-(by2-by1)*(ax1-bx1)
   v2=(bx2-bx1)*(ay2-by1)-(by2-by1)*(ax2-bx1)
   v3=(ax2-ax1)*(by1-ay1)-(ay2-ay1)*(bx1-ax1)
   v4=(ax2-ax1)*(by2-ay1)-(ay2-ay1)*(bx2-ax1)
   if((v1*v2<0) and (v3*v4<0)):
      return true
    else:
      return false

def find_point(x1,y1,x2,y2,x3,y3,x4,y4):#точка пересечения отрезков + расстояние до неё
    coord=[0]*3
    coord[0]=((x1*y2-x2*y1)*(x4-x3)-(x3*y4-x4*y3)*(x2-x1))/((y1-y2)*(x4-x3)-(y3-y4)*(x2-x1))
    coord[1]=((y3-y4)*coord[0]-(x3*y4-x4*y3))/(x4-x3)
    coord[2]=math.sqrt((x1-coord[0])**2+(y1-coord[1])**2)
    return coord
def find_mir(Cx,Cy,Ax,Ay,A1x,A1y,A2x,A2y):
    #for point C(laser: C, A-C) and wall (A1,A2),D=A2-A1, A between A1-A2; B normal, new point C+2fD, f=(Ay-Cy+(Cx-Ax)By/Bx)/(Dy-ByDx/Bx)
    #new way (A, C+2fD-A)
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

def Laser_step(r,l1):
  l2=Laser
  mas1=[0]*3
  l2.Direction[0]=l1.Position[0]+(l1.Direction[0]-l1.Position[0])*200/(math.sqrt((l1.Direction[0]-l1.Position[0])**2+(l1.Direction[1]-l1.Position[1])**2))
  l2.Direction[1]=l1.Position[1]+(l1.Direction[1]-l1.Position[1])*200/(math.sqrt((l1.Direction[0]-l1.Position[0])**2+(l1.Direction[1]-l1.Position[1])**2))  
  l1.Direction[0]=l2.Direction[0] #сдвигаем второй конец отрезка за пределы поля
  l1.Direction[1]=l2.Direction[1]
  mas1[0]=l1.Position[0]
  mas1[1]=l1.Position[1]
  if(cross(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],0,0,0,99)): #ищем пересечение с границей поля
        mas1=find_point(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],0,0,0,99)
  if(cross(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],0,0,99,0)):
    mas1=find_point(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],0,0,99,0)
  if(cross(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],99,99,99,0)):
    mas1=find_point(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],99,99,99,0)
  if(cross(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],99,99,0,99)):
    mas1=find_point(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],99,99,0,99)
  l1.Direction[0]=mas1[0]
  l1.Direction[1]=mas1[1]
  l2.Position[0]=mas1[0]
  l2.Position[1]=mas1[1]
  l2.Direction[0]=mas1[0]
  l2.Direction[1]=mas1[1]
  rmin=200
  for i in range (r.Number_of_walls):#ищем ближайшее пересечение с зеркалом
    if(cross(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],r.Nodes[i][0],r.Nodes[i][1],r.Nodes[int((i+1)%r.Number_of_walls)][0],r.Nodes[int((i+1)%r.Number_of_walls)][1])):
      mas1=find_point(l1.Position[0],l1.Position[1],l1.Direction[0],l1.Direction[1],r.Nodes[i][0],r.Nodes[i][1],r.Nodes[int((i+1)%r.Number_of_walls)][0],r.Nodes[int((i+1)%r.Number_of_walls)][1]))
      if(mas1[2]<rmin):
            rmin=mas1[2]
            l2.Position[0]=mas1[0]
            l2.Position[1]=mas1[1] #запоминаем точку пересечения
            mas2=find_mir(l1.Position[0],l1.Position[1],mas1[0],mas1[1],r.Nodes[i][0],r.Nodes[i][1],r.Nodes[int((i+1)%r.Number_of_walls)][0],r.Nodes[int((i+1)%r.Number_of_walls)][1]))
            l2.Direction[0]=mas2[0]#запоминаем направление
            l2.Direction[1]=mas2[1]
  return l2

