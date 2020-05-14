import speech_recognition as sr
r = sr.Recognizer()
 harvard = sr.AudioFile("Recording.wav")
 with harvard as source:
     audio = r.record(source)
     # type(audio)
 #r.recognize_google(audio)
#with sr.Microphone() as source:
 #   print("say something")
#    audio = r.listen(source)
#    print("okay")
try:
    text = r.recognize_google(audio)
    print("Text: " + text)
    f = open("output.txt", "a+")
    f.write("\n" + text)
    f.close
except:
    pass
