import cv2
import numpy as np
cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()
while True:
    diff = cv2.absdiff(frame1,frame2)
    #convert color to Gray
    a  = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur =  cv2.GaussianBlur(a, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations =3)
    
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #cv2.drawContours(frame1, contours, -1, (255,0,0), 2)
    for contour in contours: 
        (x,y,w,h) = cv2.boundingRect(contour)
        
        if cv2.contourArea(contour) < 700:
            continue
        
        cv2.rectangle(frame1, (x,y), (x+w, y +h ), (127,255,212), 2)
        
        cv2.putText(frame1, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX,
              1, (127,255,212), 3     
                   )
    cv2.imshow("Enter", frame1)
    frame1 = frame2
    ret,frame2 = cap.read()

    key = cv2.waitKey(1)
    if key == 27:
        break 
cv2.destroyAllWindos()
