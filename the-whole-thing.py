import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
#I set it to the voice bank in Spanish. Use test-all-voices.py to check the ones you have so you can use other banks.
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')  #Choose voiceID (bank)
#engine.setProperty('voice', 'es')  #Choose voice language? But the voice bank already determines the language...

while 1:    #Yeah I know this is poor loop handling deal with me

    with sr.Microphone() as source:
        print("Listening...")  # Prompt the user to speak
        audio = recognizer.listen(source)   #Record audio clip from Microphone

    try:
        text = recognizer.recognize_google(audio, language='es-ES')   #interpret audio to text
        print("You said:", text)
        engine.say(text)    #read text aloud
        #engine.say(text, r"path/to/file")   #use this one in case you're using an audio clip

        engine.runAndWait() #run synchronously TODO run async

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Sorry, there was an error with the request: {0}".format(e))