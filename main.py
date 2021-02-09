äventyr = {}
with open("äventyr.test.txt") as file:
    for line in file: 
      line = (line.strip())
      s = line.split (":")
      rad = int(s[0]) 
      information = s [1]
      äventyr [rad] = information 

print ("Nu börjar " + äventyr[0] +". Håll i hatten." )

poiton = 1
Slut = False
while not Slut:
  

for y in äventyr:
  line = line.split (";")
  if line [0] == "S":
    print (line[1])
    break

for x in äventyr:
  line = line.split (";")
  if line [0] == "H":
    print (line[1])


