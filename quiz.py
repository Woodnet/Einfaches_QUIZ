#
#     Author: Pulsar
#     Python-Version: 3.8.2
#     GitHub: https://github.com/Woodnet
#     Code-Editor used: Pycharm Community Edition
#     Creation-Year: 12021 (Holoän) | 2021 (gregorianisch)
#     Twitter: https://twitter.com/7Pulsar
#
import os, sys, random

daten = {
    'dateinamen': {
        'quiz_fragen': "quiz_fragen_antworten.txt",
    },
    'Fragen_Antworten': [],
}

class QUIZ_APP:
    def __init__(self, status):
        self.status = status

    def QUIZ_HOME(self):
        while True:
            input('Drücke ENTER um zu starten: ')
            break
        quiz.QUIZ_starten()

    def QUIZ_starten(self):
        zähler = 1
        for frage_antwort in daten['Fragen_Antworten']:
            argumente = frage_antwort.split('$')
            Frage = argumente[0]
            Antwort = argumente[1]
            print(Frage+" %s:\n" % (zähler))
            for i in range(len(argumente)):
                if (i != 1 and i != 0):
                    print(" #>> %s" % (argumente[i]))
            print("\n")
            while True:
                __antwort = input("Deine Antwort = ")
                if (__antwort != "" and __antwort != " "):
                    quiz.p("Bist du dir sicher, dass das deine Antwort ist?")
                    y_n = input("Y/N = ")
                    if (y_n.lower() == "y" or y_n.lower() == "n"):
                        if (y_n.lower() == "y"):
                            break
                        else:
                            pass
            if (__antwort.lower() == Antwort.lower()):
                print("[+] Richtige Antwort!")
            else:
                print("[!] Falsche Antwort!")
            zähler += 1

    def fehlermeldung(self,FEHLER):
        print("(!) Fehler: %s"%(FEHLER))

    def p(self, nachricht):
        print("INFO: "+nachricht)

    def quiz_fragen_hinzufügen(self):
        try:
            datei = open(daten['dateinamen']['quiz_fragen'],'r')
            Lines = datei.readlines()
            datei.close()
            for line in Lines:
                if (line.strip() != "" and line.strip() != ""):
                    daten['Fragen_Antworten'].append(line.strip())
        except Exception as e:
            quiz.fehlermeldung(e)
            sys.exit()

if __name__ == '__main__':
    try:
        try:
            os.system("cls") #Windows -default
        except Exception as e:
            os.system("clear") #Linux OS

        status = True
        quiz = QUIZ_APP(status)
        quiz.quiz_fragen_hinzufügen()
        quiz.QUIZ_HOME()
    except KeyboardInterrupt:
        print("\nINFO: Keyboard Interrupt")

    n = input(">>> ")
