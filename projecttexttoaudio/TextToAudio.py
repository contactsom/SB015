from gtts import gTTS

print("Read from Text to Audio")
f=open("simplilearn.text")
x=f.read()

audio=gTTS(text=x,slow=False)
audio.save("simplilearn.mp3")

print("Audio File Created , Let Play")