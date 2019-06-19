#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on March 26 00:30:50 2018

@author: Diana Rocha Botello
"""
from time import sleep
import os
import pyglet
import speech_recognition as sr
from gtts import gTTS
import nltk
from nltk import grammar, parse
from nltk import load_parser 
from nltk.parse.generate import generate

class VoiceController():
	# text to speech (gTTS and playsound player) 
	def speak(self, audioString, audioName):
		tts = gTTS(text=audioString, lang='es')
		tts.save(audioName)
		music = pyglet.media.load(audioName, streaming=False)
		music.play()
		sleep(music.duration) #prevent from killing
		os.remove(audioName) #remove temperory file

	#get text from speaker (speech_recognition)
	def getText(self, order):
		r = sr.Recognizer()
		mic = sr.Microphone()
		print(order)
		self.speak(order, "pedirOpcion.mp3")
		with mic as source:
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)
		texto = r.recognize_google(audio, language="es-MX")        
		print("Dijiste: " + texto)
		return texto;

	def validateGrammar(self, speakerText):
		try:
			sem = -1
			tokens = speakerText.split()
			cp = load_parser('semGato.fcfg', trace=0)
			tree = cp.parse_one(tokens)
			if tree is not None:
				sem = tree.label()['sem']
			return sem
		except ValueError:
			return sem

	def getPosition(self, treeRoot):
		if treeRoot != -1:
			strSem = str(treeRoot)
			pos =  strSem[strSem.find('(')+1 : strSem.find(')')]
			print(pos)
			return pos
		else:
			self.speak("No es una opción válida", "noValida.mp3")
			return -1

	def getOrder(self, orden):
		sem = -1
		while sem == -1:
			speakerOrder = self.getText(orden)
			if speakerOrder == 'salir' or speakerOrder == 'muestra movimientos':
				sem = speakerOrder
			else:
				sem = self.validateGrammar(speakerOrder.lower())
				#print(sem)
				pos = self.getPosition(sem)
				return pos
		return sem

if __name__ == "__main__":
	#validateGrammar(self, speakerText):
	pos = VoiceController().validateGrammar("tira en 2")
	pos1= VoiceController().getPosition(pos)
	#print(pos)