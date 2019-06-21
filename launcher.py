#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on June 20 11:30:50 2019
Edited on June 20 11:30:50 2019

@author: Diana Rocha Botello
@author: Lorena Guadalupe Zavaleta Rivera
"""
import os

class Launcher():
    def getUserApps(self, nombre,  listCaracteristicas, voiceController):
        opcionesAplicacion = []
        voiceController.speak("Éstas son las aplicaciones que podrían interesarte", "audio")
        for element in listCaracteristicas:
            apps = self.getAppsByInterest(element[0])
            for app in apps:
                opcionesAplicacion.append(app)
                voiceController.speak(str(app), "audio")
        #print(opcionesAplicacion)
        voiceController.speak("¿Cuál deseas utilizar ahora?", "audio")
        option = "error"
        seleccion = -1
        while seleccion == -1:
            while option == "error":
                option = voiceController.getText()
                if option == "error":
                    voiceController.speak("¿Cuál aplicación deseas utilizar ahora?", "audio")
            seleccion = self.launcApp(option, opcionesAplicacion)
            if seleccion == -1:
                option = "error"
                voiceController.speak("Esa aplicación es inválida.", "audio")

    def  getAppsByInterest(self, element):
        opcionesAplicacion = []
        if element=="videojuegos":
            opcionesAplicacion.append('Steam')
        if element=="juegosInfantiles":
            opcionesAplicacion.append('Disney latino')
        if element=="series":
            opcionesAplicacion.append('Netflix')
            opcionesAplicacion.append('Amazon video')
        if element=="caricaturas":
            opcionesAplicacion.append('Netflix')
            opcionesAplicacion.append('YouTube')
        if element=="musica":
            opcionesAplicacion.append('Spotify')
        if element=="redesSociales":
            opcionesAplicacion.append('Instagram')
            opcionesAplicacion.append('Facebook')
        if element=="tareas":
            opcionesAplicacion.append('Power Point')
            opcionesAplicacion.append('Word')
        if element=="navegarIntenet":
            opcionesAplicacion.append('Google')
        if element=="correo":
            opcionesAplicacion.append('Gmail')
            opcionesAplicacion.append('Outlook')
        if element=="trabajo":
            opcionesAplicacion.append('Power Point')
            opcionesAplicacion.append('Word')
        return opcionesAplicacion

    def launcApp(self, app, opcionesAplicacion):
        bandera = -1
        for element in opcionesAplicacion:
            if element == app:
                bandera = 1
                self.openApp(app)
        return bandera

    def openApp(self, app):
        if app =="Steam":
            os.system("start C:\Steam")
        if app =="Disney latino":
            os.system(r"start chrome https://aja.disney.com/juegos")
        if app =="Netflix":
            os.system("start chrome www.netflix.com")
        if app =="Amazon video":
            os.system(r"start chrome https://www.primevideo.com")
        if app =="Spotify":
            os.system(r"start C:\Users\lore_\AppData\Roaming\Spotify\Spotify.exe")
        if app =="Instagram":
            os.system(r"start chrome www.instagram.com")
        if app =="Facebook":
            os.system(r"start chrome www.facebook.com")
        if app =="Power point":
            os.system("start Powerpnt.exe")
        if app =="Word":
            os.system("start Winword.exe")
        if app =="Google":
            os.system(r"start chrome www.google.com")
        if app =="Gmail":
            os.system(r"start chrome www.google.com/gmail/")
        if app =="Outlook":
            os.system(r"start chrome www.outlook.com")
        if app  == "YouTube":
            os.system(r"start chrome www.youtube.com")