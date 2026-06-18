from gtts import *

text=gTTS(input("Enter the text"))
text.save("test.mp3")