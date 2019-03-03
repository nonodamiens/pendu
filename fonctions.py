import donnees

def enrPseudo(pseudo):
    pseudo=str(pseudo)
    if len(pseudo) < 1 and len(pseudo) > 10 :
        erreur="erreur"
        return erreur
    else :
        with open("scores.txt","r") as score:
            scores=score.read()
        nouveau=scores.find(pseudo)
        if nouveau >= 0:
            interval=nouveau+len(pseudo)
            bestScore=scores[interval:interval+2]
            print("Bonour {}, votre meilleur score est : {}".format(pseudo,bestScore))
            return bestScore
        else:
            print("Bienvenue {}.".format(pseudo))
            pseudo=pseudo+"00"
            with open("scores.txt", "a") as objet:
                objet.write(pseudo)
            bestScore="00"
            return bestScore

def choisirMot():
    import random
    liste=donnees.mots
    mot=random.choice(liste)
    return mot

def enrScore(score,pseudo):
    score=str(score)
    if len(score) == 1:
        score="0"+score
    with open("scores.txt","r") as scores:
        scores=scores.read()
    debut=scores.find(pseudo)
    fin=debut+len(pseudo)+2
    old=scores[debut:fin]
    new=pseudo+score
    newScores=scores.replace(old,new)
    with open("scores.txt","w") as oldScores:
        oldScores.write(newScores)
