from grammar import VoiceController

if __name__ == "__main__":
	#validateGrammar(self, speakerText):
	vc = VoiceController()
	vc.speak("Hola, ¿Cómo te llamas?", "audio")
	#print(pos)