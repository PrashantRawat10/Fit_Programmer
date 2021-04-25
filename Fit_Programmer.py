#FIT PROGRAMER
#9-5(working hours)
#drink water,rest eyes,physical exercise and smile at the end of the day

from pygame import mixer
from time import time
from datetime import datetime

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
 
#for saving the data in a text file
def saving_data(details):
    now=datetime.now()
    with open("entries.txt", "a") as f:
        f.write(f"{details} {now}\n")
        print()

if __name__=='__main__':
    drink_water=time()
    rest_eyes=time()
    physical_exercise=time()
    smile_time=time()
    while True:
        if (time()-drink_water)>7200:                 #time in seconds(2 hours)
            print("TIME TO DRINK WATER!!! Type okay to stop")
            musiconloop('water.mp3','stop')
            drink_water=time()
            saving_data("Drank water at")
        if (time()-rest_eyes)>3600:                   #time in seconds(1 hours)
            print("CLOSE YOUR EYES FOR 2 MINUTE  Type done after opening your eyes")
            musiconloop('melody.mp3', 'done')
            rest_eyes=time()
            saving_data("Eyes closed for 2 minutes at")
        if(time()-physical_exercise)>10800:           #time in seconds(3 hours)
            print("Take a walk for 5 minutes   Type walked to stop")
            musiconloop('alarm.mp3', 'walked')
            physical_exercise=time()
            saving_data("Physical activity done at")
        if(time()-smile_time)>28800:                  #time in seconds(8 hours) , at the end of the working day
            print("SMILE BECAUSE LIFE IS BEAUTIFUL!!  and type thankyou")
            musiconloop('smile.mp3', 'thankyou')
            smile_time=time()
            saving_data("Smiled at")

            


    