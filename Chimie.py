#info : pantalla de 320 x 240
from kandinsky import*
x = 45
y = 43
f = 18
aaa = False
def Pxl(x,y,aaa):
  set_pixel(x,y,color(0,0,0))
  set_pixel(x,y+65,color(0,0,0))
  if aaa == False:
    set_pixel(x,y+130,color(0,0,0))

def Pxl_AAA(x,y,aaa):
  x = 45
  y = 42
  for i in range(2):
    x = 45
    for v in range(18):
      set_pixel(x,y+130,color(0,0,0))
      x = x+1
    y = y+3
  x = 73
  y = 42
  for n in range(2):
    for v in range(2):
      for i in range(18):
        set_pixel(x,y+130,color(0,0,0))
        x = x+1
        y = y+1
      x = x-18
      y = y-17
    x = 14
    y = 22
  x = 73
  y = 42
  for n in range(2):
    for v in range(2):
      for i in range(18):
        set_pixel(x,y+130,color(0,0,0))
        x = x+1
        y = y-1
      x = x-17
      y = y+18
    x = 14
    y = 62

def pxl_dede(x,y):
  x = 45
  y = 43
  for i in range(2):
    x = 45
    for v in range(18):
      Pxl(x,y,aaa)
      x = x+1
    y = y+1
  x = 75
  y = 44
  for v in range(2):
    for i in range(18):
      set_pixel(x,y+65,color(0,0,0))
      x = x+1
      y = y+1
    x = x-18
    y = y-17
  x = 75
  y = 44    
  for v in range(2):
    for i in range(18):
      set_pixel(x,y+65,color(0,0,0))
      x = x+1
      y = y-1
    x = x-17
    y = y+18

#AcideCarboxylique------------------------------------------------------
def ACE(x,y,f,aaa):
  draw_string("Acide Carboxylique",0,0)
  draw_string("R  C",34,35)
  draw_string("O",93,17)
  draw_string("OH",91,47)
  
  draw_string("Cetone",0,65)
  draw_string("R  C",34,100)
  draw_string("O",93,82)
  draw_string("C",91,115)
  
  draw_string("Ester",0,130)
  draw_string("R  C",34,165)
  draw_string("O",93,147)
  draw_string("O-R'",91,180)
  
  draw_string("Suffixe",215,0)
  draw_string("acide-...",215,20)
  draw_string(" -oique",215,38)
  draw_string("...-one",215,75)
  draw_string("nbr R...",215,145)
  draw_string("oate de",215,163)
  draw_string("nbr R'-yle",215,181)
  dib(x,y,f,aaa)
  tab()
#-----------------------------------------------------------------------

#Aldehide---------------------------------------------------------------
def AAA(x,y,f,aaa):
  tab()
  draw_string("Aldehide",0,0)
  draw_string("R  C",34,35)
  draw_string("O",93,17)
  draw_string("H",91,47)
  
  draw_string("Amide",0,65)
  draw_string("R  C",34,100)
  draw_string("O",93,82)
  draw_string("N",91,115)
  
  draw_string("Alcene",0,130)
  draw_string("C  C",34,165)
  
  draw_string("Suffixe",215,0)
  draw_string("...-anal",215,21)
  draw_string("...-amide",215,75)
  draw_string("...-ene",215,145)
  dib(x,y,f,aaa)
  Pxl_AAA(x,y,aaa)
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
def ALC_AMD(x,y,aaa):
  tab()
  draw_string("Alcool",0,0)
  draw_string("   OH",34,35)
  
  draw_string("Amine",0,65)
  draw_string("   N",34,100)
  
  draw_string("Suffixe",215,0)
  draw_string("...-ol",215,21)
  draw_string("...-amine",215,75)
  pxl_dede(x,y)
#-----------------------------------------------------------------------

#dibujar ACE-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def dib(x,y,f,aaa):
  x = 45
  y = 43
  f = 18
#lineas horizontales----------------------------------------------------
  for i in range(2):
    x = 45
    for v in range(18):
      Pxl(x,y,aaa)
      x = x+1
    y = y+1
  x = 73
  y = 44
#-----------------------------------------------------------------------
#lineas diagonales  dobles arriba---------------------------------------
  for i in range(2):
    for i in range(f):
      Pxl(x,y,aaa)
      x = x+1
      y = y-1
    y = 37
    x = 75
    f = 16
  x = 73
  y = 44
#-----------------------------------------------------------------------
#lineas diagonales para abajo-------------------------------------------
  for i in range(2):
    for i in range(18):
      Pxl(x,y,aaa)
      x = x+1
      y = y+1
    x = 73
    y = 43
#-----------------------------------------------------------------------
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

#tableau----------------------------------------------------------------
def tab():
  for i in range(320):
    set_pixel(212,i,color(0,0,0))
    if i > 211:
      set_pixel(i,20,color(0,0,0))
      set_pixel(i,65,color(0,0,0))
      set_pixel(i,140,color(0,0,0))
#-----------------------------------------------------------------------
def borrar():
  for y in range(22):
    draw_string("                                ",0,10*y)
print("1C: Methane \n2C: Ethane \n3C: Propane \n4C: Butane \n5C: Pentane \n6C: Hexane")
wait = input("continuer \nATRAS para salir")
while 1 :
  ACE(x,y,f,aaa)
  wait = input()
  borrar()
  aaa = True
  AAA(x,y,f,aaa)
  wait = input()
  borrar()
  ALC_AMD(x,y,aaa)
  wait = input()  
  borrar()
  aaa = False
