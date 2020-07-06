from math import *
def suiteag(a,b,uo) :
  u=uo
  top=int(input("Nombre de termes ? "))
  for n in range(top) :
    u=a*u+b
    print(n+1,"->",u)
  print("suite auxiliaire :")
  r=float(b/(a-1))
  print("vn = un + ",r)
  print("Etude :")
  print("vn+1 = un+1+",r)
  print("vn+1=",a,"un+",b,"+",r)
  print("vn+1=",a,"un+",b+r)
  print("vn+1=",a,"(un+",(b+r),"/",a,")")
  print("vn+1=",a,"(un+",(b+r)/a,")")
  print("vn+1=",a,"vn")
  print("vn geometrique de raison ", a)
  print("v0= ", uo+r)
  print("vn=",uo+r,"x",a,"^n")
  print("un=vn-",r)
  print("un=",uo+r,"x",a,"^n +",-r)
  print("limite un ",-r)
  
def isprime(n):
  if type(n)!=int or n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def diviseurs(n):
  if type(n)!=int or n<1:
    return None
  if n==1:
    return [1]
  liste=[1]
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      liste.append(i)
      if n//i!=i:
        liste.append(n//i)
  return sorted(liste)+[n]

def pgcd(a,b):
  if type(a+b)!=int:
    return None
  while b!=0:
    a,b=b,a%b
  return abs(a)

def ppcm(a,b):
  if type(a+b)!=int:
    return None
  return a*b//pgcd(a,b)

def quotient(a,b):
  if type(a+b)!=int:
    return None
  liste=[]
  while b!=0:
    liste.append(a//b)
    a,b=b,a%b
  return liste

def bezout(a,b):
  if pgcd(a,b)!=1:
    return None
  u0, v0, u1, v1 = 1, 0, 0, 1
  while b:
    a, (q, b) = b, divmod(a, b)
    u0, v0, u1, v1 = u1, v1, u0 - q * u1, v0 - q * v1
  return u0, v0

def diophant(a,b,c):
  d=pgcd(a,b)
  if pgcd(d,c)!=d:
    print("Pas de solutions")
  if abs(a)<abs(b):
    a,b=b,a
  e,f,g=a//d,b//d,c//d
  u,v=bezout(e,f)
  print("(",u*g,"+",f,"k)*",a,"+","(",v*g,"-",e,"k)*",b,"=",c)
  
print("differentes fonction utiles:\n bexout, diophant,\n isprime, suiteag")
