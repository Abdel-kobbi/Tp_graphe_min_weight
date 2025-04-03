from random import randint

def generer_matrice(length):
    matrice = []
    for i in range(length):
        line = []
        for j in range(length):
            line.append(0)
        matrice.append(line)
        
    for i in range(length):
        for j in range(i,length):
            if i != j:
                value = randint(1, 100)
                matrice[i][j] = value
                matrice[j][i] = value
    return matrice

matrice = generer_matrice(4)

for line in matrice:
    print(line)