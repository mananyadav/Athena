#!/usr/bin/python
__author__ = 'Manan Yadav'

def main():
    """
    the main program
    """
    import os
    from bin import words
    import speech_recognition as sr

    try:
        word = sr.Recognizer()
        os.system('clear')
        with sr.Microphone() as source:
            os.system('clear')
            print("Listening...")
            audio = word.listen(source)
        try:
            from bin import words
            userInput = word.recognize_google(audio)
            print("I heard : " + userInput)
            words.main(str(userInput))
        except sr.UnknownValueError:
            pass

        os.system('python athena.py')
    except Exception:
        pass

if __name__ == '__main__':
    main()
