import serial, time
from vc import captureImage


#setup
baudrate = 9600
port = 'COM15'
ser = serial.Serial()

def configure():
    ser.baudrate = baudrate
    ser.port = port
    ser.open()
    return True

def sread():
    #p_taken = False

    while True:
        try:
            data = ser.read()
            if data == b'\01':
                print('Image..')
                captureImage()
                time.sleep(5)
                break
               # p_taken = True
            else:
                print('No signal..')
                sread()
        except Exception as e:
            print(e)
            
def main():
    try:
        configure()
        sread()
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    main()
