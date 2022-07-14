from getkey import getkey
import os, time
import random

y = 1
height = 5
score = 0
once = 1

while True:
  key = getkey()
  if key == "w":
    y = y + 1 
  if key == "s":
    y = y - 1
#check if 
  if y == 6:
    y = 5
  elif y < 1:
    y = 1
#generate star

  place = 0
  if once == 1:
    y = 1
    place = random.randint(2,5)
    once = once + 1
  
  counter = 5
  os.system("clear")
  while counter != 0:
    if counter == y:
      print("🤢")
    if place == y:
      score = score + 1
      place = random.randint(1,5)
      while place != y:
        place = random.randint(1,5)
    if place == counter:
      print("🪙")
    else:
      print(" ")
    counter = counter - 1
  print("use w and s to move up and down\nyour score is " + str(score))
  time.sleep(0.000001)
