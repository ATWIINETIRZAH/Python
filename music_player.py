from replit import audio

import os, time



def play():
  source = audio.play_file('audio.wav')
  source.paused = False 
  while True:
    plays=int(input("press 2 if you want to stop playing:"))
    if plays==2:
      source.paused= True
      return
    else:
      continue

while True:
  os.system("clear")
  print("MyPOD Music Player")
  time.sleep(1)
  print("Press1 to play")
  time.sleep(1)
  print("Press2 to exit")
  ans=int(input())
  if ans==1:
    print("playing music:")
    play()
  elif ans==2:
    print("end tunes.")
    exit()
  else:
    continue