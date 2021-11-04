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

#Navn_fil_1 = str(input("Hva heter filen? :"))
#Navn_nyfil_2 = str(input("Hva skal den nye filen hete? :"))

#try:
#    org_fil = open(Navn_fil_1, "r", encoding = "UTF-8")
 #   ny_fil = open(Navn_nyfil_2, "w")

#   for linje in org_fil:
 #     lu_mellomrom = linje.strip()
#
 #       delstreng = lu_mellomrom.find("From:") # index
  #      start_linje = lu_mellomrom.find("<") # index
 #       slutt_linje = lu_mellomrom.find(">") # index
#
 #       if delstreng != -1:
 #           resultat = lu_mellomrom[start_linje + 1 : slutt_linje]
 #           if resultat.find("@") != -1:
 #                print(resultat)
#            else:
 #               print("\n")

#    org_fil.close()


#Oppgave c
