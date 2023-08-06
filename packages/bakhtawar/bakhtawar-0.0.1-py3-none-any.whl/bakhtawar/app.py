import pyautogui as pg
import time  

def magic(t):
    t=int(t*60/11)
    for i in range(t):              
        pg.moveRel(100,0,duration=2)    
        pg.moveRel(0,300,duration=2)    
        pg.leftClick()   
        x,y= pg.position()
        r,g,b=pg.pixel(x,y)   
        print(r,g,b)     
        if r==0:     
            pg.press('tab')               
            pg.press('space') 
        else: 
            pass 
        pg.moveRel(-100,0,duration=2)  
        pg.moveRel(0,-300,duration=2)  
        pg.leftClick()     
        x,y= pg.position()
        r,g,b=pg.pixel(x,y)   
        print(r,g,b)     
        if r==0:     
            pg.press('tab')               
            pg.press('space') 
        else: 
            pass 
        pg.leftClick()
