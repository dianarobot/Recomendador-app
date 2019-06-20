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

	vc.speak("¿Qué estudias: la Secundaria, la Preparatoria o la Universidad?", "audio")
	#print(pos)