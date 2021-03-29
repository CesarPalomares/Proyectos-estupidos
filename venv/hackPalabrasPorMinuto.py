import pynput,time,pytesseract,cv2,numpy
from PIL import Image, ImageGrab

pytesseract.pytesseract.tesseract_cmd ='C:\Program Files\Tesseract-OCR\ tesseract'

def getWords():
    img = ImageGrab.grab(bbox=(60,400,1600,1000))

    #img.show()

    imgText=pytesseract.image_to_string(cv2.cvtColor(numpy.array(img), cv2.COLOR_BGR2GRAY),  lang ='eng')

    return imgText

def autowrite():
    keyboard = pynput.keyboard.Controller()
    letra = "fly relate house expert charge interview itself because job consider knowledge color low late hope significant understand " \
            "business home where entire tonight want heavy such sell way employee by civil hold executive become station successful enough " \
            "task exactly reflect about fear let perform "

    for x in letra:

        keyboard.press(x)
        keyboard.release(x)

def pause():
    time.sleep(5)


#main
pause()
print(getWords())



