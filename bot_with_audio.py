import speech_recognition as sr

def voice_Recognition():
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
    return r.recognize_google(audio)
        
def hello_fromBot():
    print("Bot : Hello im your bot ")
    user_name = input()
    print('Hello ' + user_name)

def save_numbers(number):
    print("This is the number " + str(number))


def mapNumbers_to_Person(person):
    print("This is the name of the person " + person )
    

#In this main we are going to use the bot functions
#main
hello_fromBot()
Save_numbers = []
Save_person = []

#variable for store the audio
Bot_audio = voice_Recognition()
#print("This is your voice " + str(Bot_audio))

#Get the voice from the audio
for i in range(0,3):
    numbers = int(input())
    save_numbers(numbers)
    Save_numbers.append(numbers)
    
    print("Give me the person name")
    person = input(Bot_audio)
    mapNumbers_to_Person(person)
    Save_person.append(person)
    
print(Save_numbers)
print(Save_person)
# Mapping the list values
PhoneBook = dict(zip(Save_numbers,Save_person))
print(PhoneBook)






   
    
    