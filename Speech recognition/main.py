import speech_recognition as sr

r = sr.Recognizer()
#Usar microfone
with sr.Microphone() as fonte:
    print('Diga alguma coisa: ')
    #Escuta o microfone
    audio = r.listen(fonte)

    #Transforma o audio em uma frase
    frase = r.recognize_google(audio, language='pt-BR')
    
    try:
        print('Você disse: ' + frase)
    except:
        print('Não entendi')

