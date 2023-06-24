import speech_recognition as sr
import pydub
import subprocess
import time
import os

r=sr.Recognizer()
while True:
	recorder = subprocess.Popen(['arecord', '--format=S16_LE', '--rate=16000', '--file-type=wav', 'example.wav'])
	time.sleep(1)
	with sr.AudioFile('example.wav') as source:
		time.sleep(5)
		audio = r.record(source)
		try:
			text = r.recognize_google(audio)
		except sr.UnknownValueError:
			continue
		if text=='':
			continue
		if text=='exit mirror':
			os.system('mmpm mm-ctl --stop')
			print(text)
			break;
		print(text)
		output = subprocess.check_output(['./new_gpt', text])
		my_zenity = subprocess.Popen(['zenity', '--info', '--text={}'.format(output.decode('utf-8').strip()), '--width=600', '--height=600'])
		time.sleep(10)
		subprocess.call(['kill', str(my_zenity.pid)])
		subprocess.call(['rm', 'example.wav'])
