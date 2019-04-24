#for point C(laser: C, A-C) and wall (A1,A2),D=A2-A1, A between A1-A2; B normal, new point C+2fD, f=(Ay-Cy+(Cx-Ax)By/Bx)/(Dy-ByDx/Bx)
#new way (A, C+2fD-A)
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


def cross(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2):
   v1=(bx2-bx1)*(ay1-by1)-(by2-by1)*(ax1-bx1)
   v2=(bx2-bx1)*(ay2-by1)-(by2-by1)*(ax2-bx1)
   v3=(ax2-ax1)*(by1-ay1)-(ay2-ay1)*(bx1-ax1)
   v4=(ax2-ax1)*(by2-ay1)-(ay2-ay1)*(bx2-ax1)
   if((v1*v2<0) and (v3*v4<0)):
      return true
    else:
      return false

    

def Laser_step(r,l1):
  l2=Laser
  
  return l2

