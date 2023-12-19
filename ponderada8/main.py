from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
from deep_translator import GoogleTranslator


def speech_to_text():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
      recognizer.adjust_for_ambient_noise(source)
      print("Capturando áudio...")
      audio = recognizer.listen(source)
      try:
          print("Convertendo fala em texto...")
          text = recognizer.recognize_google(audio, language="pt-BR")
          return text
      except sr.UnknownValueError:
          print("Não foi possível reconhecer a fala.")
      except sr.RequestError as e:
          print("Erro na requisição ao Google Web Speech API; {0}".format(e))

def text_to_speech(text):
  tts = gTTS(text, lang='pt')
  tts.save('1.mp3')
  sound_file = '1.mp3'
  playsound(sound_file)

def translate(text):
   translator = GoogleTranslator(source='pt', target='iw')
   translated = translator.translate(text=text)
   return translated

while True:
  entrada = speech_to_text()
  print(entrada)
  try:
    translate(entrada)
    text_to_speech(entrada)
    time.sleep(1)
  except Exception as e:
    print(e)