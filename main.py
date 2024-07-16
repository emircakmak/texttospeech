from gtts import gTTS
import os

myText = "Welcome to my basic text to speech python program"
language = 'en'

myObj = gTTS(text=myText, lang=language, slow=False)
myObj.save("test.mp3")
os.system("start test.mp3")