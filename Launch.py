from random import randint

import FindAndOpenAWebPage

"""
This class allows to launch the bot (FindAndOpenAWebSite). There
is a word list of potential key words that the user can enter to
find our web site: 'http://melanie-osteo-animalier.fr/. Randomly, 
it'll create a the name of a search that a user can make, and it 
will call the bot's class (FindAndOpenAWebPage) with the web site's
name and the search name that the user enter in google.
@author: Kierian Tirlemont
"""

if __name__ == "__main__":
    wordListOsteo = ["osteopathe animalier", "Ostéopathe animalier","osteo animalier", "Ostéo animalier"]
    wordListLocation = ["Eure", "Oise", "Ile-de-France", "78", "95", "93", "92", ""]
    wordListAnimal = ["chevaux", "chien", "chat", "bovin", "NAC", "nouveaux animaux de compagnie", ""]
    wordListName = ["Melanie", "Pierre", "Melanie Pierre", "", "", ""]
    wordListAnnexe = ["tarif", "déroulement d'une consultation", "quand consulter", "contact", "ostéopathie",
                      "", "", "", "", ""]

    for i in range(0,10):
        positionIntOsteo = randint(0, 3)
        osteo = wordListOsteo[positionIntOsteo]
        positionIntLocation = randint(0, 7)
        location = wordListLocation[positionIntLocation]
        positionIntAnimal = randint(0, 6)
        animal = wordListAnimal[positionIntAnimal]
        positionIntName = randint(0, 5)
        name = wordListName[positionIntName]
        positionIntAnnexe = randint(0, 9)
        annexe = wordListAnnexe[positionIntAnnexe]
        researchWords = osteo + ' ' + location + ' ' + animal + ' ' + name + ' ' + annexe
        var = FindAndOpenAWebPage
        var.FindAndOpenAWebPage.__init__(var, 'http://melanie-osteo-animalier.fr/', researchWords)
        var.FindAndOpenAWebPage.mainApp(var)

