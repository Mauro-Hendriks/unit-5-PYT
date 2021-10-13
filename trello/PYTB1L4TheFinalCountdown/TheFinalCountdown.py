import time

import vlc
  

import pafy 

def countdown(tijd):
    
    while tijd:
        mins, secs = divmod(tijd, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        tijd -= 1
      
    url = "https://www.youtube.com/watch?v=kpfisl0VFm4?t=1"
  
    video = pafy.new(url)
  
    best = video.getbest()
  
    media = vlc.MediaPlayer(best.url)
  
    media.play()
  
  

tijd = input("Enter the time in seconds: ")
  

countdown(int(tijd))
