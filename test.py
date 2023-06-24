import speech_recognition as sr
import pyttsx3
import subprocess

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
def Jarvis_run(command):
    if(command=="update"):
        command=command+" -y"
    res = subprocess.run(command.split(), stdout=subprocess.PIPE)
    print(res)

while True:
    try:
        # Prompt the user to speak
        print("Please say something...")
        
        # Use the microphone as source for input
        with sr.Microphone() as source:
            
            # Wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=1)
            
            # Listens for the user's input
            audio = r.listen(source)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            print("Did you say:", MyText)
            if("Jarvis" in MyText or "jarvis" in MyText):
                Jarvis_run(MyText)
            SpeakText(MyText)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("Unknown error occurred")
    
    except KeyboardInterrupt:
        print("Program interrupted by user")
        break
