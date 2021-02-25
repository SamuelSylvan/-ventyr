import time
import os
import random
äventyr = {}


äventyr_testloop = False

file = ""
äventyret=""
while äventyr_testloop == False:
  print ("Vilket äventyr vill du spela?")
  print ("1. Skogsäventyret")
  print ("2. skriskoäventyret")
  äventyret = input()
  os.system ("clear") 
  time.sleep(0.25)
  äventyr_test = äventyret.isdigit() 
  if äventyr_test == False:
    os.system ("clear")
    print ("Ogiltligt val")
    input()
    os.system ("clear") 
    time.sleep(0.25)
  else: 
    äventyret = int (äventyret)
    if äventyret >  2:
      print ("Ogiltligt val")
      input()
      os.system ("clear")
      time.sleep(0.25)
    else: 
      äventyr_testloop = True





if äventyret == 1:
  file = "testäventyret.txt"
if äventyret == 2:
  file = "skriskoäventyret.txt" 

os.system("clear")
time.sleep(0.25)
with open (file) as file:
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
    for i in range (antal*20):
      print (nummer,end="\r", flush = True)
      time.sleep(0.1) 
      nummer = nummer + 1 
      if nummer > antal:
        nummer = 1
    rand = (random.randint(1, antal))
    print(rand)
    position =  int (text[rand+2])