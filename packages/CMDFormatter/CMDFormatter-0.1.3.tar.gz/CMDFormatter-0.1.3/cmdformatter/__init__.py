import random
import time
import os
Fore = '['

CMD_RED = '31'
CMD_GREEN = '32'
CMD_BLACK = '0'
CMD_YELLOW = '33'
CMD_BLUE = '34'
CMD_SKYBLUE = '35'
CMD_ALL = [CMD_RED,CMD_GREEN,CMD_BLACK,CMD_YELLOW,CMD_BLUE,CMD_SKYBLUE]


def write(text = "" , color=CMD_BLACK , colorList=[] , cyclic=False , durationInMilis=0 , totalTime=0  , end="\n"):
    j = 0
    if(len(colorList)==0):
        colorList = [color] 
    if(totalTime != 0 ):
        durationInMilis = totalTime*1000 / len(text)
    for i in text:
        if cyclic:
            color = colorList[j]
        else:
            color = colorList[random.randint(0,len(colorList) - 1)]
        print(Fore + color + 'm' , end="" , flush=True)
        print(i , end="" , flush=True)
        print(Fore + CMD_BLACK + 'm' , end="" , flush=True)
        j = (j+1 )% len(colorList)
        if(durationInMilis !=0):
            time.sleep(durationInMilis/1000)
    print(end)

def ScreenFlush():
    os.system('cls')