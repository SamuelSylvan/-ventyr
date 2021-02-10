äventyr = {}
with open("äventyr.test.txt") as file:
    for line in file: 
      line = (line.strip())
      s = line.split (":")
      rad = int(s[0]) 
      information = s [1]
      äventyr [rad] = information 

print ("Nu börjar " + äventyr[0] +". Håll i hatten." )
text = "hej"
position = 1
Slut = False
while not Slut:
  text = äventyr [position]
  text = text.split (";")
  if text [0] == "S":
    print (text[1])
    Slut = True
  if text [0] == "H":
    print (text[1])
    position = int (text [2])
  if text [0] == "V":
    print (text[1])

   

# 'information = information.split(";")
  # if information [0] == "S":
  #   print (information[1])
  #   Slut = True
  # if line [0] == "H":
  #   print (line[1])

# for y in äventyr:
#   line = line.split (";")
#   if line [0] == "S":
#     print (line[1])
#     break

# for x in äventyr:
#   line = line.split (";")
#   if line [0] == "H":
#     print (line[1])


# '