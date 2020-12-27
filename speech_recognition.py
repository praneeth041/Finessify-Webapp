import speech_recognition

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("Say the activity you want to input and its priority(High/Low)")
    audio = recognizer.listen(source)

print("Activity : TO BE DONE")
print("Priority : TO BE DONE")
print("You have said")
print(recognizer.recognize_google(audio))