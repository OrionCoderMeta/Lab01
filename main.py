# classe DOMANDA
import random


class Domanda:
    def __init__(self,descrizione, difficolta, corretta, risposta1, risposta2, risposta3):
        self.risposta1 = risposta1
        self.risposta2 = risposta2
        self.risposta3 = risposta3
        self.corretta = corretta
        self.difficolta = difficolta
        self.descrizione = descrizione
        self.domande = [risposta1, risposta2, risposta3, corretta]

    def playone(self):
        # Le domande devono essere random, poi le printo
        random.shuffle(self.domande)
        print(f"Livello {self.difficolta}) {self.descrizione}\n"
                f"         1. {self.domande[0]}\n"
                f"         2. {self.domande[1]}\n"
                f"         3. {self.domande[2]}\n"
                f"         4. {self.domande[3]}\n")

        # Questo è un ciclo per avere il numero della risposta corretta
        i = 0
        right = -1
        while i < 4:
            if self.domande[i] == self.corretta:
                right = i+1
                break
            else:
                i += 1

        # Adesso faccio un check per vedere se ha fatto corretto
        guess = int(input("Inserisci la risposta: "))
        if guess == right:
            print("Risposta corretta!")
            return True
        else:
            print("Risposta sbagliata! La risposta corretta era ", right)
            return False

def game(list):
    random.shuffle(list)
    flag = True
    punteggio = 0

    while flag:
        for domanda in list:
            if domanda.difficolta == punteggio:
                flag = domanda.playone()
                random.shuffle(list)
                if not flag:
                    break
                punteggio += 1
            else:
                continue

    print(f"Hai totalizzato {punteggio} punti!")
    username = input("Inserisci il tuo nickname: ")
    with open("punti.txt", "a", encoding="utf-8") as file:
        file.write(f"{username} {punteggio}\n")

def main():
    domande = []

    with open("domande.txt", "r", encoding="utf-8") as file:
        righe = [riga.strip() for riga in file.readlines() if riga.strip()]  # Rimuove righe vuote

    for i in range(0, len(righe), 6):  # Ogni domanda ha 6 righe
        descrizione = righe[i]
        difficolta = int(righe[i+1])
        corretta = righe[i+2]
        risposta1 = righe[i+3]
        risposta2 = righe[i+4]
        risposta3 = righe[i+5]

        quest = Domanda(descrizione, difficolta, corretta, risposta1, risposta2, risposta3)
        domande.append(quest)

    game(domande)












main()