from tkinter import *
from math import *

# Dimension Fenetre ----------------------------------------------------------
hauteur=400
longueur=600

# Particules -----------------------------------------------------------------
# Format : particules=['particuleX','particuleY','dX','dY','masse','index','taille']
particules=[[125,100,2,3,12,1,50],[200,125,-1,3,6,2,70]]

# Energie Cinétique ----------------------------------------------------------
ECb=0.5*particules[0][4]*(particules[0][2]+particules[0][3])**2
ECr=0.5*particules[1][4]*(particules[1][2]+particules[1][3])**2

# Libre parcours -------------------------------------------------------------
distances=[]
Lp=0

# Variables pour le temps ----------------------------------------------------
t=0
told=0
temps=0

# Pression -------------------------------------------------------------------
f=(particules[0][2]+particules[0][3])*(particules[0][4])
perimetre=1600
Pression=f/perimetre

# Relation des Gaz Parfaits --------------------------------------------------
surface=150000
RelationGP=Pression*surface

# Fonction moyenne d'une liste -----------------------------------------------
def moyenne(liste):
  res=0
  for i in liste:
    res+=i
  res/=len(liste)
  return res

# Mouvement de la particule bleue --------------------------------------------
def mouvementparticule1():
  global particules,t,told,temps,Lp

  particules[0][0]+=particules[0][2]
  particules[0][1]+=particules[0][3]

  # Collisions avec les murs -------------------------------------------------
  if particules[0][0]<50:
    particules[0][2]*=-1
  if particules[0][0]+particules[0][6]>550:
    particules[0][2]*=-1
  if particules[0][1]<50:
    particules[0][3]*=-1
  if particules[0][1]+particules[0][6]>350:
    particules[0][3]*=-1 
  
  # Collision entre les deux particules --------------------------------------
  if particules[0][0]<=particules[1][0]+particules[1][6] and particules[0][0]+particules[0][6]>=particules[1][0] and particules[0][1]+particules[0][6]>=particules[1][1] and particules[0][1]<=particules[1][1]+particules[1][6]:
    particules[0][2]*=-1
    particules[1][2]*=-1
    particules[0][3]*=-1
    particules[1][3]*=-1
    t=temps-told
    told=temps
    distances.append(t*sqrt(particules[0][2]**2+particules[0][3]**2))
    distances.append(t*sqrt(particules[1][2]**2+particules[1][3]**2))
    Lp=moyenne(distances)

  myCanvas.coords(particule1,particules[0][0],particules[0][1],particules[0][0]+particules[0][6],particules[0][1]+particules[0][6])
  temps+=1
  tempsaff.config(text="Temps entre 2 collisions : "+str(t))
  tempsaff.update()
  LpAff.config(text="Distance moyenne entre 2 collisions : "+str(int(Lp)))
  LpAff.update()
  myCanvas.after(10,mouvementparticule1)
  
  
# Mouvement de la particule rouge -------------------------------------------
def mouvementparticule2():
  global particules
  
  particules[1][0]+=particules[1][2]
  particules[1][1]+=particules[1][3]

  # Collisions avec les murs ------------------------------------------------
  if particules[1][0]<50:
    particules[1][2]*=-1
  if particules[1][0]+particules[1][6]>550:
    particules[1][2]*=-1
  if particules[1][1]<50:
    particules[1][3]*=-1
  if particules[1][1]+particules[1][6]>350:
    particules[1][3]*=-1 

  myCanvas.coords(particule2,particules[1][0],particules[1][1],particules[1][0]+particules[1][6],particules[1][1]+particules[1][6])
  myCanvas.after(10,mouvementparticule2)

# Script Principal ----------------------------------------------------------
reservoir=Tk()
reservoir.title("Reservoir à Particules")
myCanvas=Canvas(reservoir,bg='grey',height=hauteur,width=longueur)
myCanvas.pack(side=TOP,padx=0,pady=0)
Rectangle=myCanvas.create_rectangle(50,50,550,350,fill='white')
particule1=myCanvas.create_oval(particules[0][0],particules[0][1],\
                             particules[0][0]+particules[0][6],particules[0][1]+particules[0][6],width=2,fill='blue')
particule2=myCanvas.create_oval(particules[1][0],particules[1][1],\
                             particules[1][0]+particules[1][6],particules[1][1]+particules[1][6],width=2,fill='red')         
quitButton=Button(reservoir,text='Quitter',command=reservoir.quit)
quitButton.pack()
ECbleu=Label(reservoir,text='Energie cinétique bleu : '+str(ECb)+' J')
ECbleu.pack()
ECrouge=Label(reservoir,text='Energie cinétique rouge : '+str(ECr)+ ' J')
ECrouge.pack()
tempsaff=Label(reservoir)
tempsaff.pack()
LpAff=Label(reservoir)
LpAff.pack()
P=Label(reservoir,text='Pression = '+str(round(Pression,3)))
P.pack()
Relation=Label(reservoir,text='PS = '+str(int(RelationGP)))
Relation.pack()
mouvementparticule1()
mouvementparticule2()
reservoir.mainloop()