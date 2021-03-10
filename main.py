import time
import os
import random
äventyr = {}
början = True
while början == True:  
  äventyr_testloop = False
  file = ""
  äventyret = "" 
  while äventyr_testloop == False:
    print ()
    print ("Vilket äventyr vill du spela?")
    print ("1. Skogsäventyret")
    print ("2. Skriskoäventyret")
    print ("3. Herrgårdsäventyret")
    print ("4. Hundäventyret")
    print ("Eller vill du sluta spela?")
    print ("5. Avsluta")
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
      if äventyret >  5:
        print ("Ogiltligt val")
        input()
        os.system ("clear")
        time.sleep(0.25)
      else: 
        äventyr_testloop = True
  if äventyret == 3:
    file = "herrgårdsäventyret.txt"      
  if äventyret == 1:
   file = "testäventyret.txt"
  if äventyret == 2:
    file = "skriskoäventyret.txt" 
  if äventyret == 4:
    file = "hundäventyret.txt"
  if äventyret == 5:
    os.system ("clear")
    break
  os.system("clear")
  time.sleep(0.25)
  with open (file) as file:
    for line in file: 
      line = (line.strip())
      s = line.split (":")
      rad = int(s[0]) 
      information = s [1]
      äventyr [rad] = information 
  print()
  print ("Nu börjar " + äventyr[0] +". Håll i hatten." )
  input()
  os.system("clear")
  time.sleep(0.25) 
  saker = set([])
  position = 1
  Slut = False
  
  while not Slut:
   
    text = äventyr [position]
    text = text.split (";")
    if text [0] == "S":
      print()
      print (text[1])
      Slut = True
      input()
      os.system ("clear")
      time.sleep(0.25)
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
      time.sleep(0.75)
      os.system("clear")
      time.sleep(0.25)
    if text [0] == "FS":
      Split = text [1].split (",")
      längd = len(Split)
      längd = längd - 1
      antal_föremål = text [2]
      antal_föremål = int (antal_föremål)
      print ()
      print (text [3])
      sak_nummer = 1
      while antal_föremål > 0:
        print (" Sak nummer " + str (sak_nummer) + ":")
        sak = input()
        if not sak in Split:
          print ("Ogiltligt val.")
        else : 
          saker.add(sak)
          antal_föremål = antal_föremål -1
          sak_nummer = int (sak_nummer) + 1
          position = int (text[4])
      input()
      os.system("clear")
      time.sleep
    if text[0]  == "F":

      Föremål = text [1].split()
      saker.update(set(Föremål))
      print()
      print (text[2])
      position = int (text [3])
      input()
      os.system("clear")
      time.sleep(0.25) 
    if text[0] == "FB":
      print()
      print (text[2])
      Föremål_Behov = text [1].split()
      if set(Föremål_Behov).issubset(saker):
        saker = saker.difference(set(Föremål_Behov))
        position =int (text [3])
        os.system("clear")
        time.sleep(0.25)
      else : 
        position = int (text [4])
        os.system("clear")
        time.sleep(0.25)
    if text [0] == "":
      print()
      print (text[2])
      Föremål_Behov = text [1].split()
      if set(Föremål_Behov).issubset(saker):
        position =int (text [3])
        os.system("clear")
        time.sleep(0.25)
      else : 
        position = int (text [4])
        os.system("clear")
        time.sleep(0.25)