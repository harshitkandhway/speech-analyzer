import speech_recognition as sr
filename="ramesh_interview.wav"
r=sr.Recognizer()
with sr.AudioFile(filename) as source:
	audio_data = r.record(source)
	text = r.recognize_google(audio_data)
try:
    print("Text: " + text)
    f = open("output.txt", "a+")
    f.write("\n" + text)
    f.close
except:
    pass