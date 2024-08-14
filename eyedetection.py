import cv2

trained_data=cv2.CascadeClassifier("haarcascade_eye.xml")

img=cv2.imread("images.jpg")

face=trained_data.detectMultiScale(img)

for x,y,h,w in face:

    cv2.rectangle(img,(x,y),(x+w,y+h),(255,1,1),2)

cv2.imshow("welcome",img)

cv2.waitkey(0)