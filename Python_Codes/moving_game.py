import os
import time

size = 15

def show(c, b, x, y) : 
  for i in range(size) : 
    for j in range(size) :
      if (x == i) and (y == j) :
        print(c,end="")
      else :
        print(b,end="")
    print()

def move(key, character, blank, x, y) : 
  os.system('cls')

  if key == 'w' :
    if x != 0 :
      x -= 1
  elif key == 's' : 
    if x != size - 1 : 
      x += 1
  elif key == 'a' : 
    if y != 0 : 
      y -= 1
  elif key == 'd' : 
    if y != size - 1 : 
      y += 1
  elif key == 'z' : 
    exit(0)
  show(character, blank, x, y) 
  return x, y


def main() :
  character = "■"
  blank = "□"
  x, y = 0, 0
  
  show(character, blank, x, y)
  while True :
    key = str(input())
    if key == 'z' :
      break
    else : 
      x, y = move(key, character, blank, x, y)
    
      



if __name__ == "__main__" :
  start = time.time()
  main()
  end = time.time()
  print("Playing Time : {}s".format(round(end-start, 2)))