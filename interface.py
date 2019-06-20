#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 19 11:30:50 2019
Edited on June 19 11:30:50 2019

@author: Diana Rocha Botello
@author: Lorena Guadalupe Zavaleta Rivera
"""

from grammar import VoiceController

if __name__ == "__main__":
	vc = VoiceController()
	#response = "error"
	#while response != "Hola":
	#		print("RecApp: Nadie me ha dicho hola :( ")
	#		response = vc.getText()
	#		print(response)

	#vc.speak("Hola, ¿Cómo te llamas?", "audio")
	#response = "error"
	#while response == "error":
	#		response = vc.getText()
	#		print(response)
	#		if response == "error":
	#			vc.speak("¿Cuál es tu nombre?", "audio")
	### AGREGAR NOMBRE EN LA KB

	#Ocupación
	vc.speak("¿Eres estudiante o trabajador?", "audio")
	response = vc.getResponse()
	print(response)
	### AGREGAR OCUPACIÓN EN LA KB

	#Trabajador
	vc.speak("¿Eres trabajador activo o jubilado?", "audio")
	response = vc.getResponse()
	print(response)
	### AGREGAR OCUPACIÓN EN LA KB

	# Estudiante
	vc.speak("¿Eres estudiante de Jardín de niños o de Primaria?", "audio")
	response = vc.getResponse()
	print(response)
	### AGREGAR OCUPACIÓN EN LA KB

	vc.speak("¿Eres estudiante de: la Secundaria, la Preparatoria o la Universidad?", "audio")
	response = vc.getResponse()
	print(response)
	### AGREGAR OCUPACIÓN EN LA KB