import cv2
import pathlib


clf = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(2)

while True:
    _,frame = camera.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = clf.detectMultiScale(
        gray,
        scaleFactor =1.1,
        minNeighbors =5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE 
    )
    for (x,y,width,height) in face:
        cv2.rectangle(frame,(x,y),(x+width,y+height),(255,255,0),2)
    
    cv2.imshow("faces",frame)
    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
    
