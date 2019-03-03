import fonctions
import donnees


# Demande du pseudo

retour="erreur"
while retour=="erreur":
    pseudo=input("quel est votre pseudo :")
    retour=fonctions.enrPseudo(pseudo)
bestScore=int(retour)

# Boucle générale

rejouer = True
while rejouer:
    
    mot=fonctions.choisirMot()
    cache="*"*len(mot)
    motCache=str()
    essai=donnees.nbEssai
    print("Voici le mot à trouver : {}".format(cache))

    # demander une lettre au joueur
    perdu=False

    while mot != cache:
        if essai > 0:
            lettre=input("choisir une lettre ou un mot :")
            try:
                lettre=float(lettre)
                print("lettre ou mot merci")
            except:        
                if len(lettre) == 1:
                    if mot.count(lettre) == 0:
                        essai=essai-1
                        print("raté")
                    else:
                        essai=essai-1
                        print("gagné")
                        # afficher le mot avec lettre trouvées et cachées
                        newcache=str()
                        c=0
                        for l in mot:
                            if l == lettre:
                                newcache=newcache+lettre
                                c+=1
                            else:
                                newcache=newcache+cache[c]
                                c=c+1
                        cache=newcache
                        print(newcache)
                elif lettre == mot:
                    cache=mot
                else:
                    print("1 seule lettre à la fois, merci !")
        else:
            cache=mot
            perdu=True
    if perdu:
        print("vous avez perdu")
        print("le mot était : {}.".format(mot))
    else:
        print("bravo vous avez trouvé !")
        print("Votre score est de {} point(s).".format(essai))
        if essai>bestScore:
            fonctions.enrScore(essai,pseudo)
            bestScore=essai

    rep=True

    while rep:

        rejouer=input("Rejouer ? (y/n) : ")
        if rejouer == "y":
            rejouer=True
            rep=False
        elif rejouer == "n":
            rejouer = False
            rep=False
        else:
            print("Réponse incorrect")
print("Merci d'avoir joué")
    
