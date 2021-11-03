class Norge:
    def __init__(self, sporsmal_txt, svar_alternativ, rett_svar):
        self.sporsmal_txt = sporsmal_txt
        self.svar_alternativ = svar_alternativ
        self.rett_svar = int(rett_svar)

    def __str__(self):
        alle_alternativ = '\n'.join(self.svar_alternativ)
        return f'Spørsmål: {self.sporsmal_txt} \n \n'\
                f'Alternativ: \n' \
                f'{alle_alternativ}'

    def sjekk_svar(self, svar):
        if svar == self.rett_svar:
            print("Det er rett!\n")
        else:
            print("Sorry, det er feil\n")


if __name__ == '__main__':
    a = ["Oslo", "Stavanger", "Bergen", "Trondheim", "Tromsø"]

    sporsmal1 = "Hva er hovedstanden i Norge?"
    svar1 = 1

    sporsmal2 = "I hvilken by ligger UIS i?"
    svar2 = 2

    q1 = Norge(sporsmal1, a, svar1)
    print(q1)
    qq1 = int(input("Skriv inn svaret ditt her: "))
    q1.sjekk_svar(qq1)

    q2 = Norge(sporsmal2, a, svar2)
    print(q2)
    qq2 = qq1 = int(input("Skriv inn svaret ditt her: "))
    q2.sjekk_svar(qq2)



#hjelp prøver å forstå dette her marie WHERE ARE YOU
