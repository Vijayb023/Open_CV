import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX

 
if __name__ == '__main__' :
 
    im = cv2.imread("sample.jpg")
    org = (50, 50) 
    fontScale = 1
    thickness = 2
    color = (255, 0, 0) 
    image = cv2.putText(im, 'Draw box and press enter', org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
    showCrosshair = False
    fromCenter = False
    r = cv2.selectROI("Image", im, fromCenter, showCrosshair)
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    

    cv2.imshow("Image", imCrop)
    cv2.imwrite('Image.jpg',imCrop)
    cv2.waitKey(0)