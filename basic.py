import cv2
import numpy as np
import face_recognition


# step one to load image
# step 2 find the image
#
# imgshubhi = face_recognition.load_image_file('images/shubhi.jpg')
# imgshubhi = cv2.cvtColor(imgshubhi,cv2.COLOR_BGR2RGB)
# imgTest = face_recognition.load_image_file('images/subhi test.jpg')
# imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)


imgbill = face_recognition.load_image_file('images/bill1.jpg')
imgbill = cv2.cvtColor(imgbill,cv2.COLOR_BGR2RGB)
imgbTest = face_recognition.load_image_file('images/bill1.jpg')
imgbTest = cv2.cvtColor(imgbTest,cv2.COLOR_BGR2RGB)




faceloc = face_recognition.face_locations(imgbill)[0]
encodebill = face_recognition.face_encodings(imgbill)[0]
# if len(encodeshub) > 0:
#     biden_encodesub = encodeshub[0]
# else:
#    print("No faces found in the image!")
#    quit()
cv2.rectangle(imgbill,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)



facelocTest = face_recognition.face_locations(imgbTest)[0]
encodeTest = face_recognition.face_encodings(imgbTest)[0]
cv2.rectangle(imgbTest,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodebill],encodeTest)
# distance
facedis = face_recognition.face_distance([encodebill],encodeTest)



print(results,facedis)

cv2.putText(imgbTest,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)



cv2.imshow('bille',imgbill)
cv2.imshow('Shubham Test',imgbTest)
cv2.waitKey(0)