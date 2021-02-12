if __name__ == "__main__":
    fichier = open('input.txt', 'r')
    content = fichier.read()
    mon_tableau = [i for i in content.split('\n')]
    compteurmdpok = 0

    for a in mon_tableau:
        x = a.split(' ')[1]
        y = a.split('-')[1]
        nombre_mini = int(a.split('-')[0])
        nombre_max = int(y.split(' ')[0])
        mdp = a.split(': ')[1]
        lettre = x[:-1]
        parametre1 = 0
        parametre2 = 0


        if lettre == nombre_mini and lettre!= nombre_max or lettre != nombre_mini and lettre == nombre_max:
            compteurmdpok = compteurmdpok +1
        print(compteurmdpok)




