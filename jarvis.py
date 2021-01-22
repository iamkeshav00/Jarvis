import speech_recognition as sr
import pyttsx3,pywhatkit,datetime 
#creating a listener
listener=sr.Recognizer() #creating a recognizer to recognize what i m talking
engine= pyttsx3.init() # initialising a speaking engine

def talk(text): #this function converts the text to speech
    engine.say(text)
    engine.runAndWait()
def take_command():#this function take the command from the user and convert it into text
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source) #getting voice data from mic
            command = listener.recognize_google(voice) #using google api to convert speech to text
            command=command.lower()#converting text into lowercase
            if 'jarvis' in command:
                command=command.replace("jarvis","")
                print(command)
                
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    if "play" in command:
        song=command.replace('play','')
        
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk('current time is '+time)
    elif 'single' in command:
        talk("yes sir I am single ,but i do want to get in relationship with siri")
    elif 'repeat' in command:
        repeat=command.replace("repeat","")
        talk(repeat)
    elif "who is siri" in command:
        talk("she is my love")
talk("hello sir")
talk("how may i help you?")
run_alexa()