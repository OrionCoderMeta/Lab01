import random

# Classe Users
class User:
    def __init__(self, username, punteggio):
        self.username = username
        self.punteggio = punteggio

    def __str__(self):
        return f"{self.nome} {self.punteggio}"


# Classe DOMANDA
class Domanda:
    def __init__(self,descrizione, difficolta, corretta, risposta1, risposta2, risposta3):
        self.risposta1 = risposta1
        self.risposta2 = risposta2
        self.risposta3 = risposta3
        self.corretta = corretta
        self.difficolta = difficolta
        self.descrizione = descrizione
        self.domande = [risposta1, risposta2, risposta3, corretta]

    def playone(self): # metodo per le partite
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
    max_punti = 4 # può essere modificato in futuro

    # controllare se una domanda è giusta o sbagliata
    while flag:
        for domanda in list:
            if punteggio > max_punti:
                break
            elif domanda.difficolta == punteggio:
                flag = domanda.playone()
                random.shuffle(list) # importante richiamarlo perchè anche se prima avevo saltato una domanda, adesso posso ripescarla
                if not flag:
                    break
                punteggio += 1
            else:
                continue

    # stampa finale e overwrite del punteggio .txt
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

    # riordino per punteggio il file punti.txt
    users = []
    with open("punti.txt", "r", encoding="utf-8") as file2:
        righe = file2.readlines()
        for r in righe:
            r = r.strip().split(" ")
            if len(r) == 2:  # Verifica che la riga abbia solo username e punteggio
                user = User(r[0], r[1])  # r[0] è il nome utente, r[1] è il punteggio
                users.append(user)

    # Ordina gli utenti in base al punteggio, dal più alto al più basso
    users.sort(key=lambda x: x.punteggio, reverse=True)

    # Scrivi il file riordinato
    with open("punti_ordinati.txt", "w", encoding="utf-8") as file3:
        for user in users:
            file3.write(f"{user.username} {user.punteggio}\n")

main()