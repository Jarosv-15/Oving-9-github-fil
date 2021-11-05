class Quiz:
    def __init__(self, sporsmal_txt, svar_alternativ, rett_svar):
        self.sporsmal_txt = sporsmal_txt
        self.svar_alternativ = svar_alternativ
        self.rett_svar = int(rett_svar)

    def __str__(self):
        for i in range(len(self.svar_alternativ)):
            self.svar_alternativ[i] = f"{i}: {self.svar_alternativ[i]}"
        all_alternativs = "\n".join(self.svar_alternativ)
        return f"{self.sporsmal_txt} \n" f"Svaralternativer: \n" f"{all_alternativs}" "\n"


    def sjekk_svar(self, svar):
        if svar == self.rett_svar:
            print("Det er rett!\n")
        else:
            print("Sorry, det er feil\n")

    def korrekt_svar_tekst(self):
        for i in range(len(self.svar_alternativ)):
            self.svar_alternativ[i] = self.svar_alternativ[i].replace(f"{i}:", "")
        index_svar = int(self.rett_svar)
        svar_str = (self.svar_alternativ)[index_svar]
        return f"Korrekt svar:{svar_str}"

objektliste = []

def filinfo():
    sporsmaalfil = open("sporsmaalsfil.txt", "r", )
    for linje in sporsmaalfil:
        linjer = linje.split(":")
        sporsmal_txt = linjer[0]

        svar_alternativ = []
        alternatives_str = linjer[2]
        alternatives_str = alternatives_str.replace('[', '')
        alternatives_str = alternatives_str.replace(']', '')
        alternativer_list = alternatives_str.split(',')
        for alternativ in alternativer_list:
            endelig_alternativ = alternativ.strip()
            svar_alternativ.append(endelig_alternativ)

        rett_svar = linjer[1]

        q = Quiz(sporsmal_txt, svar_alternativ, rett_svar)
        objektliste.append(q)

    return objektliste

if __name__ == '__main__':
    filinfo()
    # Spillernes svar
    player1_svar = 0
    player2_svar = 0

    player1_score = 0
    player2_score = 0

    for sporsmal_txt in objektliste:
        print(sporsmal_txt)
        player1_svar = int(input("Velg et svaralternativ for spiller 1: "))
        player2_svar = int(input("Velg et svaralternativ for spiller 2: "))
        print(f" \n" f"{sporsmal_txt.korrekt_svar_tekst()} \n")

        correct_ans = int(sporsmal_txt.rett_svar)

        if player1_svar == correct_ans and player2_svar != correct_ans:
            print("Spiller 1: Riktig \nSpiller 2: Feil \n")
            player1_score += 1
        elif player1_svar != correct_ans and player2_svar == correct_ans:
            print("Spiller 1: Feil \nSpiller 2: Riktig \n")
            player2_score += 1
        elif player1_svar == correct_ans and player2_svar == correct_ans:
            print("Spiller 1: Riktig \nSpiller 2: Riktig \n")
            player1_score += 1
            player2_score += 1
        else:
            print("Spiller 1: Feil \nSpiller 2: Feil \n")

    def winner(score1, score2):
        if score1 > score2:
            return "spiller 1"
        elif score2 > score1:
            return "spiller 2"
        else:
            return "ingen"

    print(f"Spiller 1 har totalt: {player1_score} poeng \nSpiller 2 har totalt: {player2_score} poeng \n"
          f"Dette betyr at {winner(player1_score, player2_score)} er vinneren!")
