import cv2 as cv
import time
import pyautogui as pg
import numpy as np

#pg setup
pg.PAUSE = 1 #1 second sleep between consucutive commands
pg.FAILSAFE = True


def sendKey(key):
    if key == 'esc':
        pass
    else:
        w, h = pg.size()
        #pg.click(0.1*w, 0.1*h) #half from each side, top-left
        pg.moveTo(200, 100)
        pg.doubleClick()
        print('Window clicked...!!!')
        time.sleep(5)
        pg.press('s') #call to save
    
    
    

def readImage():
    fileName = input('image file name: ')
    frameName = input('Frame name: ')

    image = cv.imread(fileName, 0) #1,0,-1 for colored|grayscale|Unchanged/w alpha

    #show image
    cv.imshow(frameName, image)
    #ssendKey()  #cancel saving
    key = cv.waitKey(0) & 0xFF #for x64 platform
    if key == 27: #esc
        cv.destroyAllWindows()
    elif key == ord('s'): #save the image to a new file
        outfileName = input('Outfile name: ')
        cv.imwrite(outfileName, image)
        cv.destroyAllWindows()

def captureImage2():
    print('Capture open....')
    randomfileName = str(round(time.time()))
    capture = cv.VideoCapture(0)
   # frameName = 'helloGideon's
    taken = False
    while not taken:
        val, frame = capture.read()
        image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #display image
        cv.imshow('GM', image)
        #time.sleep(5)
        time.sleep(2)
        #sendKey(key)
        pg.moveTo(200,200)
        time.sleep(2)
        pg.click()
        time.sleep(2)
        pg.hotkey('ctrl', 'c')
        print('Win clicked')
        if cv.waitKey(0) & 0xFF == 27:
            cv.destroyAllWindows()
            
        elif cv.waitKey(0) & 0xFF == ord('s'):
            print('Key sent...')
            taken = True
            cv.imwrite('C:\\users\\foo\\Desktop\\desktop\\ts\\testFiles\\%s.jpg'%(randomfileName), image)
            #capture.release()
            cv.destroyAllWindows()
            
    #capture.release()
    #cv.destroyAllWindows()
def captureImage():
    randomfileName = str(round(time.time()))
    capture = cv.VideoCapture(0)
   # frameName = 'helloGideon'
    taken = False
    while not taken:
        val, frame = capture.read()
        image = cv.cvtColor(frame, cv.IMREAD_COLOR)
        taken = True
        cv.imwrite('C:\\users\\foo\\Desktop\\desktop\\ts\\testFiles\\%s.jpg'%(randomfileName), image)
        #capture.release()
        cv.destroyAllWindows()
            
    #capture.release()
    #cv.destroyAllWindows()

def main():
    #readImage()
    captureImage()

if __name__ == '__main__':
    main()
    
    
            
    
    
