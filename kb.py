#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 20 11:30:50 2019
Edited on June 20 11:30:50 2019

@author: Diana Rocha Botello
@author: Lorena Guadalupe Zavaleta Rivera
"""

from pyDatalog import pyDatalog

class KnowledgeController():

	# default constructor 
    def __init__(self):
    	# Declarar las reglas dinámicamente
    	pyDatalog.load("""
    		persona(X) <= trabajador(X)
    		persona(X) <= estudiante(X)
    		trabajador(X) <= activo(X)
    		trabajador(X) <= jubilado(X)
    		estudiante(X) <= preescolar(X)
    		estudiante(X) <= primaria(X)
    		estudiante(X) <= secundaria(X)
    		estudiante(X) <= media_superior(X)
    		estudiante(X) <= universidad(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', 0) <= persona(X)
    		tiene_interes(X, 'juegosInfantiles', -1) <= persona(X)
    		tiene_interes(X, 'series', 4) <= persona(X)
    		tiene_interes(X, 'caricaturas', -2) <= persona(X)
    		tiene_interes(X, 'musica', 2) <= persona(X)
    		tiene_interes(X, 'redesSociales', 2) <= persona(X)
    		tiene_interes(X, 'tareas', 1) <= persona(X)
    		tiene_interes(X, 'navegarIntenet', 4) <= persona(X)
    		tiene_interes(X, 'correo', 2) <= persona(X)
    		tiene_interes(X, 'trabajo', 1) <= persona(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', -5) <= trabajador(X)
    		tiene_interes(X, 'juegosInfantiles', -5) <= trabajador(X)
    		tiene_interes(X, 'series', -1) <= trabajador(X)
    		tiene_interes(X, 'caricaturas', -5) <= trabajador(X)
    		tiene_interes(X, 'musica', 2) <= trabajador(X)
    		tiene_interes(X, 'redesSociales', 1) <= trabajador(X)
    		tiene_interes(X, 'tareas', -5) <= trabajador(X)
    		tiene_interes(X, 'navegarIntenet', 4) <= trabajador(X)
    		tiene_interes(X, 'correo', 4) <= trabajador(X)
    		tiene_interes(X, 'trabajo', 4) <= trabajador(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', 2) <= estudiante(X)
    		tiene_interes(X, 'juegosInfantiles', 2) <= estudiante(X)
    		tiene_interes(X, 'series', 3) <= estudiante(X)
    		tiene_interes(X, 'caricaturas', 1) <= estudiante(X)
    		tiene_interes(X, 'musica', 3) <= estudiante(X)
    		tiene_interes(X, 'redesSociales', 3) <= estudiante(X)
    		tiene_interes(X, 'tareas', 4) <= estudiante(X)
    		tiene_interes(X, 'navegarIntenet', 4) <= estudiante(X)
    		tiene_interes(X, 'correo', 2) <= estudiante(X)
    		tiene_interes(X, 'trabajo', -5) <= estudiante(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', -5) <= activo(X)
    		tiene_interes(X, 'juegosInfantiles', -5) <= activo(X)
    		tiene_interes(X, 'series', -2) <= activo(X)
    		tiene_interes(X, 'caricaturas', -5) <= activo(X)
    		tiene_interes(X, 'musica', 3) <= activo(X)
    		tiene_interes(X, 'redesSociales', 1) <= activo(X)
    		tiene_interes(X, 'tareas', -5) <= activo(X)
    		tiene_interes(X, 'navegarIntenet', 4) <= activo(X)
    		tiene_interes(X, 'correo', 4) <= activo(X)
    		tiene_interes(X, 'trabajo', 5) <= activo(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', -5) <= jubilado(X)
    		tiene_interes(X, 'juegosInfantiles', -5) <= jubilado(X)
    		tiene_interes(X, 'series', 5) <= jubilado(X)
    		tiene_interes(X, 'caricaturas', -5) <= jubilado(X)
    		tiene_interes(X, 'musica', 4) <= jubilado(X)
    		tiene_interes(X, 'redesSociales', 3) <= jubilado(X)
    		tiene_interes(X, 'tareas', -5) <= jubilado(X)
    		tiene_interes(X, 'navegarIntenet', 4) <= jubilado(X)
    		tiene_interes(X, 'correo', 2) <= jubilado(X)
    		tiene_interes(X, 'trabajo', -5) <= jubilado(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', -5) <= preescolar(X)
    		tiene_interes(X, 'juegosInfantiles', 5) <= preescolar(X)
    		tiene_interes(X, 'series', 2) <= preescolar(X)
    		tiene_interes(X, 'caricaturas', 5) <= preescolar(X)
    		tiene_interes(X, 'musica', 1) <= preescolar(X)
    		tiene_interes(X, 'redesSociales', -5) <= preescolar(X)
    		tiene_interes(X, 'tareas', -3) <= preescolar(X)
    		tiene_interes(X, 'navegarIntenet', 1) <= preescolar(X)
    		tiene_interes(X, 'correo', -5) <= preescolar(X)
    		tiene_interes(X, 'trabajo', -5) <= preescolar(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', 1) <= primaria(X)
    		tiene_interes(X, 'juegosInfantiles', 4) <= primaria(X)
    		tiene_interes(X, 'series', 3) <= primaria(X)
    		tiene_interes(X, 'caricaturas', 5) <= primaria(X)
    		tiene_interes(X, 'musica', 2) <= primaria(X)
    		tiene_interes(X, 'redesSociales', -2) <= primaria(X)
    		tiene_interes(X, 'tareas', 0) <= primaria(X)
    		tiene_interes(X, 'navegarIntenet', 2) <= primaria(X)
    		tiene_interes(X, 'correo', -2) <= primaria(X)
    		tiene_interes(X, 'trabajo', -5) <= primaria(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', 4) <= secundaria(X)
    		tiene_interes(X, 'juegosInfantiles', -2) <= secundaria(X)
    		tiene_interes(X, 'series', 5) <= secundaria(X)
    		tiene_interes(X, 'caricaturas', 2) <= secundaria(X)
    		tiene_interes(X, 'musica', 4) <= secundaria(X)
    		tiene_interes(X, 'redesSociales', 3) <= secundaria(X)
    		tiene_interes(X, 'tareas', 3) <= secundaria(X)
    		tiene_interes(X, 'navegarIntenet', 3) <= secundaria(X)
    		tiene_interes(X, 'correo', 1) <= secundaria(X)
    		tiene_interes(X, 'trabajo', -5) <= secundaria(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', 5) <= media_superior(X)
    		tiene_interes(X, 'juegosInfantiles', -5) <= media_superior(X)
    		tiene_interes(X, 'series', 4) <= media_superior(X)
    		tiene_interes(X, 'caricaturas', 0) <= media_superior(X)
    		tiene_interes(X, 'musica', 5) <= media_superior(X)
    		tiene_interes(X, 'redesSociales', 5) <= media_superior(X)
    		tiene_interes(X, 'tareas', 4) <= media_superior(X)
    		tiene_interes(X, 'navegarIntenet', 4) <= media_superior(X)
    		tiene_interes(X, 'correo', 3) <= media_superior(X)
    		tiene_interes(X, 'trabajo', 0) <= media_superior(X)
    	""")
    	pyDatalog.load("""
    		tiene_interes(X, 'videojuegos', 5) <= universidad(X)
    		tiene_interes(X, 'juegosInfantiles', -5) <= universidad(X)
    		tiene_interes(X, 'series', 5) <= universidad(X)
    		tiene_interes(X, 'caricaturas', -2) <= universidad(X)
    		tiene_interes(X, 'musica', 5) <= universidad(X)
    		tiene_interes(X, 'redesSociales', 5) <= universidad(X)
    		tiene_interes(X, 'tareas', 5) <= universidad(X)
    		tiene_interes(X, 'navegarIntenet', 4) <= universidad(X)
    		tiene_interes(X, 'correo', 4) <= universidad(X)
    		tiene_interes(X, 'trabajo', 2) <= universidad(X)
    	""")

    	#Insertar valores vacíos por defecto
    	pyDatalog.assert_fact('persona', '')
    	pyDatalog.assert_fact('estudiante', '')
    	pyDatalog.assert_fact('jubilado', '')
    	pyDatalog.assert_fact('primaria', '')
    	pyDatalog.assert_fact('media_superior', '')
    	pyDatalog.assert_fact('trabajador', '')
    	pyDatalog.assert_fact('activo', '')
    	pyDatalog.assert_fact('preescolar', '')
    	pyDatalog.assert_fact('secundaria', '')
    	pyDatalog.assert_fact('universidad', '')

    def setData(self, estereotipo, nombre):
    	pyDatalog.assert_fact(estereotipo, nombre)

    def forgetData(self, estereotipo, nombre):
    	pyDatalog.retract_fact(estereotipo,nombre)

    def showDataByEstereotipo(self, estereotipo):
    	W = pyDatalog.ask(estereotipo+"(X)")
    	print(W.answers)

    def getMaxValues(self, nombre):
    	W = pyDatalog.ask("tiene_interes('"+nombre+"',Y,5)")
    	return W.answers[0]

    def showValues(self, nombre):
    	W = pyDatalog.ask("tiene_interes('"+nombre+"',Y,Z)")
    	print(W)

if __name__ == "__main__":
	kb = KnowledgeController()
	pyDatalog.assert_fact('estudiante', 'Juanito')
	pyDatalog.retract_fact('estudiante', 'Juanito')
	pyDatalog.assert_fact('primaria', 'Juanito')
	pyDatalog.assert_fact('universidad', 'María')

	W = pyDatalog.ask("tiene_interes('Juanito',Y,5)")
	print(W.answers)