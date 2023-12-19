from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from deep_translator import GoogleTranslator
import time

def speech_to_text():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
      recognizer.adjust_for_ambient_noise(source)
      print("Capturando áudio...")
      audio = recognizer.listen(source)
      print("Convertendo fala em texto...")
      text = recognizer.recognize_google(audio, language="pt-BR")
      return text

def text_to_speech(text):
  tts = gTTS(text, lang='pt')
  tts.save('1.mp3')
  sound_file = '1.mp3'
  playsound(sound_file)

while True:
  entrada = speech_to_text()
  print(entrada)
  translator = GoogleTranslator(source='pt', target='en')
  translated = translator.translate(text=entrada)
  print(translated)
  text_to_speech(translated)
  time.sleep(1)