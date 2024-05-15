import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from translate import Translator
import sys
import json

# enter to env .\env\Scripts\activate
# 'npm start' to run electronJS

r = sr.Recognizer()

def process_audio(lan1):
    recognized_text = ''
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            recognized_text = r.recognize_google(audio, language=lan1)
            
        except sr.UnknownValueError:
            recognized_text = "Unable to recognize speech"
            pass
        except sr.RequestError as e:
            recognized_text = "Error occurred: " + str(e)
            pass
    return recognized_text

languages = json.loads(sys.stdin.read())
TranslateFrom = languages['translateFrom']
TranslateTo = languages['translateTo']

translator = Translator(to_lang=TranslateTo, from_lang=TranslateFrom)

original_text = process_audio(TranslateFrom)
translated_text = translator.translate(original_text)
translated_text = translated_text.replace('\u02bb', "'")
translated_text = translated_text.replace('\u02bc', "'")
translated_text = translated_text.replace('&#39;', "'")

translated_data = {
    'text1' : original_text,
    'text2' : translated_text
}

# write translation to file
with open('translate_history.txt', 'a', encoding='utf-8') as file:
    file.write(f"{original_text} < === > {translated_text}\n---\n")


result = json.dumps(translated_data, ensure_ascii=False).encode('utf-8')

sys.stdout.buffer.write(result)
sys.stdout.flush()

if TranslateTo == 'uz':
    TranslateTo = 'tr'
if  TranslateFrom == 'uz':
    TranslateFrom = 'tr'
lan1 = gTTS(original_text, lang=TranslateFrom, slow=False)
lan2 = gTTS(translated_text, lang=TranslateTo, slow=False)
lan1.save('fromLan1.mp3')
lan2.save('toLan2.mp3')
playsound('toLan2.mp3')