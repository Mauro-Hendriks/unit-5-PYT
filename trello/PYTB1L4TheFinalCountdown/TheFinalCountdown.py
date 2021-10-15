import time
import webbrowser

def countdown(tijd):
    
    while tijd:
        mins, secs = divmod(tijd, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        tijd -= 1

    webbrowser.open("https://www.youtube.com/watch?v=kpfisl0VFm4", new=1)
tijd = input("Enter the time in seconds: ")
  

countdown(int(tijd))
