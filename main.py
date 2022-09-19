
import generate

scores = open("scores.txt","r")
best_scores = []
is_playing = True
print("Bonjour !\n")
while is_playing:
    print("\n\nQue souhaitez vous faire ?\n")
    print("--> 1.Nouvelle partie\n")
    print("--> 2.Voir les 10 meilleurs scores \n")
    print("--> 3.Quitter\n")

    user_choice = int(input("\n\nVotre choix: "))
    
    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        user_choice = input("\n\nVotre choix: ")
    
    if user_choice == 1:
        print("commencons")
        length = int(input("Combien de mots voulez vous taper ? (Possible qu'il y en ai légèrement plus ou moins en fonction des phrases générées"))
        words_list=generate.generate_sentences(length)

    elif user_choice == 2:
        check = open("scores.txt","r")
        checker_scores = check.read()
        if len(checker_scores)>0:
            for i in scores.read().split('\n'):
                best_scores.append(int(i))
            best_scores.sort(reverse=True)
            for i in range(len(best_scores)):
                if i == 0:
                    print("\n\n\n______________________________________________")
                    print("\n___---===Meilleur Score===---___")
                    print (f"         --> {best_scores[i]} <--")
                else:
                    print(f"{i+1}. {best_scores[i]}")
        else:
            print("Pas encore de scores :'/")
        print("______________________________________________")



