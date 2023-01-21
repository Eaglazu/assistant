
import pyttsx3
import os
import openai
import speech_recognition as sr

openai.organization = "org-nfGaYEiK1HzHuOEyvWiaxEwr"
openai.api_key = "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"
openai.Model.list()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    l = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant :")
        audio = l.listen(source)
    try:
        return l.recognize_google(audio, language = "fr-FR")
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris ce que vous avez dit.")
    except sr.RequestError as e:
        print("Erreur de service; {0}".format(e))

def texts():
  print(listen)

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

file = open("monfichier.txt", "w") 
file.write(listen) 
file.close()

with open('demande.txt', 'r') as f:
    contenu = f.read()
    print(contenu)

print(generate_text(contenu))

def reponse():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Parlez maintenant :")
        audio = r.reponse(contenu)
    try:
        return r.recognize_google(audio, language = "fr-FR")
    except sr.UnknownValueError:
        print("Désolé, je n'ai pas compris ce que vous avez dit.")
    except sr.RequestError as e:
        print("Erreur de service; {0}".format(e))