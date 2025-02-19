
class Joueur():
    '''
    Cette classe simule les choix d'un joueur et calcule ses points.

    Attributs :
        - __equipe (dict<str : int>) : l'équipe du joueur et points associés.
        - __discord (str) : le discord du joueur.

    Méthodes :
        - __init__(discord : str) -> None : construit les objets <Joueur>.
        - getEquipe() -> str : récupère l'équipe du joueur.
        - getDiscord() -> str : récupère le discord du joueur.
        - addEquipe(listePilotes : list<str>) -> None : ajoute l'équipe de pilotes représentés par leur gamertag.
        - updatePoints(generalPoints : dict<str : int>) -> None : actualise les points de l'équipe du joueur.
        - calcScore() -> int : calcule et renvoie le score du joueur.
    '''

    def __init__(self, discord : str) -> None:
        self.__equipe = {}
        self.__discord = discord
                         
    def getEquipe(self) -> str:
        return self.__equipe

    def getDiscord(self) -> str:
        return self.__discord

    def addEquipe(self, listePilotes : list) -> None:
        if len(listePilotes)%3 == 0:
            for i in listePilotes:
                self.__equipe[i] = 0
        else:
            print("Pilote.addEquipe.Erreur : listePilote fausse.")

    def updatePoints(self, generalPoints : dict) -> None:
        for i in self.__equipe:
            try:
                self.__equipe[i] = generalPoints[i]
            except:
                pass

    def calcScore(self) -> int:
        liste = [i for i in self.__equipe.values()]
        for i in range(len(liste)):
            if liste[i] == None:
                liste[i] = 0
            if i%3 == 0:
                liste[i] *= 2
        return sum(liste)