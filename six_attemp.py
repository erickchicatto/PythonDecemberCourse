import speech_recognition as sr

#Get the audio from microphone
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak :")
    audio = r.listen(source)
    
try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
    
    
    
    

