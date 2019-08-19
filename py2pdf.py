from __future__ import print_function
from PIL import Image
import PIL.Image
import cv2
from pytesseract import image_to_string
import pytesseract
from wand.image import Image
class reader:
    def __init__(self,pdf_path):
        self.pdf_path = pdf_path
        if pdf_path[-3:] == "pdf":
            reader.pdfreader()
        else:
            self.pdf_path = pdf_path
            reader.jpgreader()


    def pdfreader():
        pdf_path="raja.pdf"
        with Image(filename=pdf_path) as img:

            print('width =', img.width)
            print('height =', img.height)
            print('pages = ', len(img.sequence))
            print('resolution = ', img.resolution)
        
        with Image(filename=pdf_path, resolution=300) as pdf:
            pdf.concat(True)
            pdf.save(filename=pdf_path[:-3] + "png")
        
        img2 =cv2.imread(pdf_path[:-3] + "png",0)
        

        imS = cv2.resize(img2,(1350, 1150))
        cv2.imshow("output",imS)
        cv2.imwrite('Output Image.PNG', imS)
        cv2.waitKey(0)

        img = cv2.imread("Output Image.PNG", 0)
        ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
        print("T hreshold selected : ", ret)
        cv2.imwrite("./output_image.png", thresh)
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'
        output = pytesseract.image_to_string(PIL.Image.open('output Image.PNG').convert("RGB"), lang='eng')
        print(output)
    def jpgreader():
        img2 =cv2.imread(pdf_path,0)
        imS = cv2.resize(img2,(1350, 1150))
        cv2.imshow("output",imS)
        cv2.imwrite('Output Image.PNG', imS)
        cv2.waitKey(0)

        img = cv2.imread("Output Image.PNG", 0)
        ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
        print("T hreshold selected : ", ret)
        cv2.imwrite("./output_image.png", thresh)

        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
        TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'
        output = pytesseract.image_to_string(PIL.Image.open('output Image.PNG').convert("RGB"), lang='eng')
        print(output)
if __name__ == "__main__":
    pdf_path=input("plase enter the the file path:")    
    reader(pdf_path)
