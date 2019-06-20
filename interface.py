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
	text = "error"
	while text != "Hola":
			print("RecApp: Nadie me ha dicho hola :( ")
			text = vc.getOrder()
			print(text)

	vc.speak("Hola, ¿Cómo te llamas?", "audio")

	#Ocupación
	vc.speak("¿Eres estudiante o trabajador?", "audio")

	#Trabajador
	vc.speak("¿Eres trabajador activo o jubilado?", "audio")

	# Estudiante
	vc.speak("¿Eres estudiante de Jardín de niños o de Primaria?", "audio")

	vc.speak("¿Eres estudiante de: la Secundaria, la Preparatoria o la Universidad?", "audio")