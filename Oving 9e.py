class Quiz:
    def __init__(self, sporsmal_txt, svar_alternativ, rett_svar):
        self.sporsmal_txt = sporsmal_txt
        self.svar_alternativ = svar_alternativ
        self.rett_svar = int(rett_svar)

    def kort_svar_tekst(self):
        for i in range(len(self.alternatives)):
            self.alternatives[i] = self.svar_alternativ[i].replace(f"{i}:", "")

        index_svar = int(self.rett_svar)
        svar_str = (self.svar_alternativ)[index_svar]

        return f"Korrekt svar:{svar_str}"

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
    print(objektliste[0])
