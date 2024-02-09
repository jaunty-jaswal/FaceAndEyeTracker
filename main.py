import cv2
import matplotlib.pyplot as plt
import os
from matplotlib import ft2font
import cv2

# Enable camera
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 420)

# import cascade file for facial recognition 
# HAAR features
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyedetect = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
while True:
    response, image = capture.read()
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Getting corners around the face
    detectedFaces = facedetect.detectMultiScale(imgGray, 1.3, 4)  # scale factor, minimum neighbor: adjust as per need
    # drawing bounding box around face
    cv2.putText(image,"press x to exit",(20,20),cv2.FONT_HERSHEY_PLAIN,2,(0,200,0),3)
    for (x, y, width, height) in detectedFaces:
                                    #point1   #point2                   #color BGR #thickness
        image = cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 3)   
        text = "Face"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 2                                                #[0] width [1] height
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0] #getting width of text box 
        text_x = x + int((width - text_size[0])-100)
        text_y = y - 5
        cv2.putText(image, text, (text_x, text_y), font, font_scale, (255,0, 0), font_thickness) 
    # detecting eyes
    eyes = eyedetect.detectMultiScale(imgGray)
    for (ex, ey, ew, eh) in eyes:
        image = cv2.rectangle(image, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        text = "eye"
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        font_scale = 0.75
        font_thickness = 1
        text_size = cv2.getTextSize(text,font,font_scale,font_thickness)[0]
        text_x = ex + int(ew - text_size[0])
        text_y = ey - 5
        cv2.putText(image,text,(text_x,text_y),font, font_scale, (0,255,0),font_thickness)
    cv2.imshow('detection', image)
    if cv2.waitKey(10) & 0xFF == ord('x'):
        break
capture.release()
cv2.destroyWindow('detection')