class Norge:
    def __init__(self, sporsmal_txt, svar_alternativ, rett_svar):
        self.sporsmal_txt = sporsmal_txt
        self.svar_alternativ = svar_alternativ
        self.rett_svar = int(rett_svar)

    def kort_svar_tekst(self):
        return

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

def filinfo():
    sporsmolfil = open("sporsmaalsfil.txt", "r")


if __name__ == '__main__':



#hjelp prøver å forstå dette her marie WHERE ARE YOU
