from audioop import mul
import names
import random

from verbs_related import pronom
#import verbs_related
#print(names.get_first_name())

#print(random.choice(pronoms))
#print(multiple)

class Pronom:
    def __init__(self):
        multiple=names.get_first_name()+" et "+names.get_first_name()
        pronoms=["tu","il","elle",names.get_first_name(),"nous","vous","elles","ils",multiple]
        self.pronom=random.choice(len(pronoms))
    def return_type_self(self):
        if self.pronom==0:
            return 2
        elif self.pronom==1 or self.pronom==2 or self.pronom==3:
            return 3
        elif self.pronom==4:
            return 4
        elif self.pronom==5:
            return 5
        elif self.pronom==6 or self.pronom==7 or self.pronom==8:
            return 6

    def return_list(self):
        id_pronom = Pronom.return_type_self()
        if id_pronom == 2:
            return ["tu","tu",id_pronom]
        elif id_pronom == 3:
            return ["il",self.pronom,id_pronom]
        elif id_pronom=="4":
            return ["nous","nous",id_pronom]
        elif id_pronom==5:
            return ["vous","vous",id_pronom]
        elif id_pronom==6:
            return ["ils",self.pronom,id_pronom]

with open("verb_complete_list.txt","r",encoding='utf-8') as verbs_list:
    f=verbs_list.read().split("\n")
    print(f)