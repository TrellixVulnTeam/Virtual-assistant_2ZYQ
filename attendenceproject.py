import cv2
import numpy as np
import face_recognition
from datetime  import  datetime

# library for assistant
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib







path = 'images'
images = []
className = []
myList = os.listdir(path)
print(myList)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    className.append(os.path.splitext(cl)[0])
print(className)

# assistant code
#
def assistant():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning!")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("I am your class asistant . Please tell me how may I help you")


    def takeCommand():
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query


    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()


    if __name__ == "__main__":
        wishMe()
        while True:
            # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email to ' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "yourEmail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend . I am not able to send this email")




def findencodings(images):
    encodeList = []
    for img in images:

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def markattendence(name):
    with open('attendence.csv','r+') as f:
        mydatalist = f.readlines()
        namelist = []
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')


# markattendence('shubham')


encodeListKnown = findencodings(images)
print('encode complete')


cap = cv2.VideoCapture(0)

while True:
    sucess, img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    faceCurframe = face_recognition.face_locations(imgs)
    encodecurframe = face_recognition.face_encodings(imgs,faceCurframe)


    for encodeface,faceloc in zip(encodecurframe,faceCurframe):
        matchesb = face_recognition.compare_faces(encodeListKnown,encodeface)
        facedis = face_recognition.face_distance(encodeListKnown,encodeface)
        #print(facedis)
        matchIndex = np.argmin(facedis)


        if matchesb[matchIndex]:
            name = className[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceloc
            y1 , x2 , y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendence(name)
            assistant()


    cv2.imshow('webcam',img)
    cv2.waitKey(1)


# imgbill = face_recognition.load_image_file('images/bill1.jpg')
# imgbill = cv2.cvtColor(imgbill,cv2.COLOR_BGR2RGB)
# imgbTest = face_recognition.load_image_file('images/bill1.jpg')
# imgbTest = cv2.cvtColor(imgbTest,cv2.COLOR_BGR2RGB)
#


#
# faceloc = face_recognition.face_locations(imgbill)[0]
# encodebill = face_recognition.face_encodings(imgbill)[0]
# # if len(encodeshub) > 0:
# #     biden_encodesub = encodeshub[0]
# # else:
# #    print("No faces found in the image!")
# #    quit()
# cv2.rectangle(imgbill,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
#
#
#
# facelocTest = face_recognition.face_locations(imgbTest)[0]
# encodeTest = face_recognition.face_encodings(imgbTest)[0]
# cv2.rectangle(imgbTest,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
#
# results = face_recognition.compare_faces([encodebill],encodeTest)
# # distance
# facedis = face_recognition.face_distance([encodebill],encodeTest)


