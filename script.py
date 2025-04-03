from random import randint


#function for generate matrix 
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

# function to save matrix in txt file
def save_matrice(matrice, path):
    with open(path, "w") as file:
        file.write(str(len(matrice)) + "\n")
        for line in matrice:
            for item in line:
                file.write(str(item) + "\t")
            file.write("\n")

save_matrice(matrice, r"matrix.txt")