import time
import os
import random
äventyr = {}
with open("äventyr.test.txt") as file:
    for line in file: 
      line = (line.strip())
      s = line.split (":")
      rad = int(s[0]) 
      information = s [1]
      äventyr [rad] = information 
print ("Nu börjar " + äventyr[0] +". Håll i hatten." )
input()
os.system("clear")
time.sleep(0.25) 
position = 1
Slut = False
while not Slut:
  text = äventyr [position]
  text = text.split (";")
  if text [0] == "S":
    print (text[1])
    Slut = True
  if text [0] == "H":
    print()
    print (text[1])
    position = int (text [2])
    input()
    os.system("clear")
    time.sleep(0.25) 
  if text [0] == "V":
    print()
    print (text[1])
    val = input()
    test = val.isdigit() 
    if test == False:
      os.system ("clear")
      print ("Ogiltligt val")
      input()
      os.system ("clear") 
      time.sleep
    else:
      val = int (val)
      os.system("clear")
      time.sleep(0.25)
      antal_val = len(text)-2
      if val > antal_val:
        print ("Ogiltligt val")
        input()
        os.system ("clear")
      else: position =  int (text [val + 1]) 
  if text [0] == "T":
    print()
    antal = int(text [1])
    nummer = 1
    print (text[2])
    input()
    for i in range (antal*5):
      print (nummer,end="\r", flush = True)
      time.sleep(0.25) 
      nummer = nummer + 1 
      if nummer > antal:
        nummer = 1
    rand = (random.randint(1, antal))
    print(rand)
    position =  int (text[rand+2])