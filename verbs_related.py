import unidecode

class pronom:
    def __init__(self,pronoms):
        self.pronom = pronoms
        
    def return_terminaison_firstGroup(self):
        if self.pronom == "je":
            return "e"
        elif self.pronom == "tu":
            return "es"
        elif self.pronom == "il" or self.pronom == "elle" or self.pronom == "on":
            return "e"
        elif self.pronom == "nous":
            return "ons"
        elif self.pronom == "vous":
            return "ez"
        elif self.pronom == "ils" or self.pronom == "elles":
            return "ent"
    def return_terminaison_secondGroup(self):
        if self.pronom == "je":
            return "s"
        elif self.pronom == "tu":
            return "s"
        elif self.pronom == "il" or self.pronom == "elle" or self.pronom == "on":
            return "et"
        elif self.pronom == "nous":
            return "ssons"
        elif self.pronom == "vous":
            return "ssez"
        elif self.pronom == "ils" or self.pronom == "elles":
            return "ssent"
    def term_indre(self):
        if self.pronom == "je":
            return "s"
        elif self.pronom == "tu":
            return "s"
        elif self.pronom == "il" or self.pronom == "elle" or self.pronom == "on":
            return "t"
        elif self.pronom == "nous":
            return "ignons"
        elif self.pronom == "vous":
            return "ignez"
        elif self.pronom == "ils" or self.pronom == "elles":
            return "ignent"
    def term_soudre(self):
        if self.pronom == "je":
            return "s"
        elif self.pronom == "tu":
            return "s"
        elif self.pronom == "il" or self.pronom == "elle" or self.pronom == "on":
            return "t"
        elif self.pronom == "nous":
            return "olvons"
        elif self.pronom == "vous":
            return "olvez"
        elif self.pronom == "ils" or self.pronom == "elles":
            return "olvent"
    def basic_troisieme(self):
        if self.pronom == "je":
            return "ds"
        elif self.pronom == "tu":
            return "ds"
        elif self.pronom == "il" or self.pronom == "elle" or self.pronom == "on":
            return "d"
        elif self.pronom == "nous":
            return "sons"
        elif self.pronom == "vous":
            return "sez"
        elif self.pronom == "ils" or self.pronom == "elles":
            return "sent"
    def vaincre_convaincre(self):
        if self.pronom == "je":
            return "cs"
        elif self.pronom == "tu":
            return "cs"
        elif self.pronom == "il" or self.pronom == "elle" or self.pronom == "on":
            return "c"
        elif self.pronom == "nous":
            return "quons"
        elif self.pronom == "vous":
            return "quez"
        elif self.pronom == "ils" or self.pronom == "elles":
            return "quent"
def conjuguer(pronoun,verb):
    compare_verb = unidecode.unidecode(verb)
    pronoun = pronoun.lower()
    terminaison = pronom(pronoun)
    second_group = open("second_group.txt","r",encoding='utf-8')
    if verb[-2:] == "er" and verb != "aller":
        conjverb = verb[:-2]
        if verb[-3:] == "ger" and pronoun == "nous":
            return conjverb+"eons"
        elif verb[-3:] == "cer" and pronoun=="nous": 
            return conjverb[0:-1]+"ç"+terminaison.return_terminaison_firstGroup()
        elif verb[-4:] == "oyer" or  verb[-4:] == "uyer":
            conjverb=conjverb[::-1].replace("y","i",1)
            conjverb=conjverb[::-1]
            return conjverb+terminaison.return_terminaison_firstGroup()
        elif verb[-4:] == "eler" and not (pronoun=="nous" or pronoun=="vous") and (compare_verb=="agneler" or compare_verb=="celer" or compare_verb=="deceler" or compare_verb=="receler" or compare_verb=="ciseler" or compare_verb=="demanteler" or compare_verb=="ecarteler" or compare_verb=="encasteler" or compare_verb=="geler" or compare_verb=="degeler" or compare_verb=="congeler" or compare_verb=="surgeler" or compare_verb=="marteler" or compare_verb=="modeler" or compare_verb=="peler"):
            conjverb = conjverb[::-1].replace("e","è",1)
            conjverb = conjverb[::-1]
            return conjverb + terminaison.return_terminaison_firstGroup()
        elif verb[-4:] == "eter" and not (pronoun=="nous" or pronoun=="vous") and (compare_verb=="acheter" or compare_verb=="racheter" or compare_verb=="bégueter" or compare_verb=="corseter" or compare_verb=="crocheter" or compare_verb=="fileter" or compare_verb=="fureter" or compare_verb=="haleter"):
            conjverb = conjverb[::-1].replace("e","è",1)
            conjverb = conjverb[::-1]
            return conjverb + terminaison.return_terminaison_firstGroup()
        elif (verb[-4:] == "ecer" or verb[-4:] == "emer" or verb[-4:] == "eper" or verb[-4:] == "erer" or verb[-4:] == "eser" or verb[-4:] == "ever" or verb[-5:] == "evrer" or verb[-4:] == "ener") and not (pronoun=="nous" or pronoun=="vous"):
            conjverb = conjverb[::-1].replace("e","è",1)
            conjverb = conjverb[::-1]
            return conjverb + terminaison.return_terminaison_firstGroup()
        elif verb[-4:] == "eter" and not (pronoun=="nous" or pronoun=="vous"):
            return conjverb + "t" +terminaison.return_terminaison_firstGroup()
        elif verb[-4:] == "eler" and not (pronoun=="nous" or pronoun=="vous"):
            return conjverb + "l" + terminaison.return_terminaison_firstGroup()
        elif (verb[-5:] == "ébrer" or verb[-4:] == "écer" or verb[-5:] == "écher" or verb[-5:] == "écrer" or verb[-4:] == "éder" or verb[-5:] == "égler" or verb[-5:] == "égner" or verb[-5:] == "égrer" or verb[-5:] == "éguer" or verb[-4:] == "éler" or verb[-4:] == "émer" or verb[-4:] == "éner" or verb[-5:] == "équer" or verb[-4:] == "érer" or verb[-4:] == "éser" or verb[-4:] == "éter" or verb[-5:] == "étrer" or verb[-5:] == "évrer" or verb[-4:] == "éyer") and not (pronoun=="nous" or pronoun=="vous"):
            conjverb = conjverb[::-1].replace("é","è",1)
            conjverb = conjverb[::-1]
            return conjverb + terminaison.return_terminaison_firstGroup()    
        else:
            return conjverb+terminaison.return_terminaison_firstGroup()
    elif verb in second_group.read():
        conjverb = verb[:-1]
        if verb == "haïr":
            if (pronoun == "nous" or pronoun =="vous" or pronoun=="ils" or pronoun=="elles"):
                return conjverb+terminaison.return_terminaison_secondGroup()
            else:
                conjverb=verb[:-2]
                return conjverb+"i"+terminaison.return_terminaison_secondGroup()
        else:
            return conjverb+terminaison.return_terminaison_secondGroup()
    else:
        if verb[-2:] == "ir":
            conjverb = verb[:-2]
            return conjverb + terminaison.return_terminaison_firstGroup()
        elif verb[-3:] == "dre":
            if "i" in verb:
                if verb[-5:] == "indre":
                    conjverb = verb[:-5]
                    return conjverb + terminaison.term_indre()
                elif verb[-6:] == "soudre":
                    conjverb = verb[:-5]
                    return conjverb + terminaison.term_soudre() 
            elif verb[-6:] == "soudre":
                conjverb = verb[:-5]
                return conjverb + terminaison.term_soudre()
            else:
                conjverb = verb[:-3]
                return conjverb + terminaison.basic_troisieme()
        elif verb=="vaincre" or verb=="convaincre":
            conjverb = verb[:-3]
            return conjverb + terminaison.vaincre_convaincre()

print(conjuguer("ils","haïr"))
            


