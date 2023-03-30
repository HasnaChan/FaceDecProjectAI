from operator import truediv
import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime
from pydoc import classname
from flask import Flask,render_template,Response
# ret, img = cap.read()
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
ret,img = cap.read()
while True:
    ret, frame = cap.read()
    # return None
    # if not ret:
    #     break
    # if stage == 2:
    #     gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     gray_scale = cv2.bilateralFilter(gray_scale, 5, 1, 1)
    #     faces = Face_Cascade.detectMultiScale(img, 1.3, 5, minSize=(200,200))
    #     cv2.putText(img,f'Identity: {name}',(50,35),cv2.FONT_HERSHEY_DUPLEX,0.6,(0,0,0),3)
    #     cv2.putText(img,f'Identity: {name}',(50,35),cv2.FONT_HERSHEY_DUPLEX,0.6,(255,255,255),1)

    #     if attended == 1:
    #         cv2.putText(img, 'Attendance Inputted Successfully, have a Nice Day!', (70,70), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,0),3)
    #         cv2.putText(img, 'Attendance Inputted Successfully, have a Nice Day!', (70,70), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,255,0),1)




    #     if len(faces) > 0:
    #         for(x,y,w,h) in faces:
    #             eye_face = gray_scale[y:y+h, x:x+w]
    #             eye_face_clr = img[y:y+h, x:x+w]
    #             eyes = Eyes_Cascade.detectMultiScale(eye_face, 1.3, 5, minSize=(50,50))
    #             if blinkCount > 0:
    #                 cv2.putText(img, f'Please blink {blinkCount} time(s) to confirm Attendance', (70,70), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,0,0),3)
    #                 cv2.putText(img, f'Please blink {blinkCount} time(s) to confirm Attendance', (70,70), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,255,0),1)
    #                 ret, jpeg = cv2.imencode('.jpg', img)
    #                 img = jpeg.tobytes()
    #                 yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')
    #             if len(eyes) >= 2 and attended == 0 and blinking == 1:
    #                 blinking = 0
    #             elif len(eyes) < 2 and attended == 0 and blinking == 0:
    #                 blinkCount = blinkCount - 1
    #                 blinking = 1
    #                 cv2.waitKey(500)
    #                 print(blinkCount)
    #                 if blinkCount == 0:
    #                     markAttendance(name)
    #                     attended = 1    
    #     else:
    #         if attended == 0:
    #             cv2.putText(img, "No face detected", (70,70), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0,255,0),2)
        
    # Small_Img = cv2.resize(img,(0,0),None,0.25,0.25,interpolation = cv2.INTER_AREA)
    # Small_Img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Faces_Curr_Frame = face_recognition.face_locations(Small_Img)
    # Encode_Curr_Frame = face_recognition.face_encodings(Small_Img, Faces_Curr_Frame)
    
    # if maskNote == 1:
    #     cv2.putText(img,'For more accurate scan, please take off your mask.',(70,70),cv2.FONT_HERSHEY_DUPLEX,0.6,(0,0,0),3)
    #     cv2.putText(img,'For more accurate scan, please take off your mask.',(70,70),cv2.FONT_HERSHEY_DUPLEX,0.6,(255,255,255),1)
    
    # for Encode_Face, faceLoc in zip(Encode_Curr_Frame, Faces_Curr_Frame):
    #     matches = face_recognition.compare_faces(Encode_ListKnown, Encode_Face)
    #     Face_Distance = face_recognition.face_distance(Encode_ListKnown, Encode_Face)
    #     Match_Index = np.argmin(Face_Distance)

    #     name = Class_Names[Match_Index]

    #     if matches[Match_Index] and Face_Distance[Match_Index] <= 0.45:
    #         stage = 2
    #         maskNote = 0
    #         name = name.upper()

    #     else:
    #         cv2.putText(img,'Identity: STRANGER',(50,35),cv2.FONT_HERSHEY_DUPLEX,0.6,(0,0,0),3)
    #         cv2.putText(img,'Identity: STRANGER',(50,35),cv2.FONT_HERSHEY_DUPLEX,0.6,(255,255,255),1)

    cv2.imshow('Webcam',frame)
    cv2.waitKey(1)