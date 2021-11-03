from pygame import mixer
from datetime import datetime
from time import time

watergap=30*60 #30 minute
eyegap=20 #45 minute
exegap=70*60 #70 minute
watertaken=time()
eyedone=time()
exedone=time()

def pdf(task):
  with open("data.txt","a") as p:
    p.write(f"{task} done at {datetime.now()}\n")

def water():
  try:
    mixer.init()
    mixer.music.load("music.mp3")
    mixer.music.play()
  except:
    print("music cannot be loaded")
  a=input("please,drink water.after drinking water,type watertaken")  
  if a=="watertaken":
    try:
      mixer.music.stop()
    except:
      print("music stopped")
  pdf("water_drinked")
  

def eye():
  try:
    mixer.init()
    mixer.music.load("music.mp3")
    mixer.music.play()
  except:
    print("music cannot be loaded")
  a=input("please,do eye exercise.after doing eye exercise,type eyedone")  
  if a=="eyedone":
    try:
      mixer.music.stop()
    except:
      print("music stopped")
  pdf("eyeexe_done at")
  

def phy():
  try:
    mixer.init()
    mixer.music.load("music.mp3")
    mixer.music.play()
  except:
    print("music cannot be loaded")
  a=input("please,do phy exercise.after doing phy exercise,type phydone")  
  if a=="phydone":
    try:
      mixer.music.stop()
    except:
      print("music stopped")
  pdf("phy_exe_done at")
  
  
while(True):
  if time()-watertaken>watergap:
    water()
    watertaken=time()
  if time()-eyedone>eyegap:
    eye()
    eyedone=time()
  if time()-exedone>exegap:
    phy()
    exedone=time()