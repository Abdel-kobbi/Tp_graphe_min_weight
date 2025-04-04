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

#matrice = generer_matrice(4)


# function to save matrix in txt file
def save_matrice(matrice, path):
    with open(path, "w") as file:
        file.write(str(len(matrice)) + "\n")
        for line in matrice:
            for item in line:
                file.write(str(item) + "\t")
            file.write("\n")

#save_matrice(matrice, r"matrix.txt")

# function to read matrix from TXT file
def read_matrice(path):
    matrice = []
    with open(path, "r") as file:
        length = int(file.readline().strip("\n"))
        for line in file:
            matrice.append(list(map(int, filter(lambda x: x.isdigit(), line.split("\t")))))
    return matrice

matrice = read_matrice(r"matrix.txt")

# function to find tree solution
def find_tree_solution(matrix):
    length_matrice = len(matrix)  # Nombre de sommet
    node_solution = [randint(0, length_matrice - 1)]  # Liste des sommets inclus dans l’arbre initialiser par sommet au hasard
    tree_solution = []  # Liste des arêtes
    weight_total = 0  # Coût total

    while len(node_solution) < length_matrice:
        minValue = float("inf")
        index = float("inf")
        u = float("inf")

        for node in node_solution:
            for v, weight in enumerate(matrix[node]):
                if (weight != 0) and (v not in node_solution) and (weight < minValue):
                    minValue = weight
                    index = v
                    u = node

        if index != float("inf"):
            node_solution.append(index)
            tree_solution.append((u, index))
            weight_total += minValue
    
    return node_solution, tree_solution, weight_total

solution = find_tree_solution(matrice)
print("node solution: ",   solution[0],
      "\nTree solution: ", solution[1],
        "\nWeight total",  solution[2],
    )
