#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 19 11:30:50 2019
Edited on June 19 11:30:50 2019

@author: Diana Rocha Botello
@author: Lorena Guadalupe Zavaleta Rivera
"""

from grammar import VoiceController
from kb import KnowledgeController
from launcher import Launcher

if __name__ == "__main__":
	vc = VoiceController()
	knowb = KnowledgeController()
	launchApps = Launcher()

	response = "error"
	while response != "Hola":
			print("RecApp: Nadie me ha dicho hola :( ")
			response = vc.getText()

	vc.speak("Hola, ¿Cómo te llamas?", "audio")
	response = "error"
	while response == "error":
			response = vc.getText()
			if response == "error":
				vc.speak("¿Cuál es tu nombre?", "audio")
	name = response
	### AGREGAR PERSONA A LA KB
	knowb.setData('persona', name)
	#knowb.showDataByEstereotipo('persona')

	#Ocupación
	response = -1
	while response == -1 or response == 'no':
		vc.speak("¿Eres estudiante o trabajador?", "audio")
		response = vc.getResponse()
	#print(response)
	### AGREGAR OCUPACIÓN EN LA KB
	knowb.setData(response, name)
	#knowb.showDataByEstereotipo(response)

	if response == "trabajador":
		#Trabajador
		response = -1
		while response == -1 or response == 'no':
			vc.speak("¿Eres trabajador activo o jubilado?", "audio")
			response = vc.getResponse()
		#print(response)
		### AGREGAR TIPO DE TRABAJADOR EN LA KB
		knowb.setData(response, name)
		#knowb.showDataByEstereotipo(response)
	else:
		# Estudiante
		response = -1
		while response == -1:
			vc.speak("¿Eres estudiante de Jardín de niños o de Primaria?", "audio")
			response = vc.getResponse()
			if response == "no":
				response = -1
				while response == -1 or response == 'no':
					vc.speak("¿Eres estudiante de: la Secundaria, la Preparatoria o la Universidad?", "audio")
					response = vc.getResponse()
		#print(response)
		### AGREGAR TIPO DE Estudiante EN LA KB
		knowb.setData(response, name)
		#knowb.showDataByEstereotipo(response)

	#Obtener Características con valor 5 para el usuario
	face = knowb.getMaxValues(name)
	launchApps.getUserApps(name, face, vc)