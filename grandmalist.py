#La fonction is_grandma_list prend une liste lst en entrée.
def verifier_grandma_list(liste):
    #Pour chaque élément, elle vérifie s'il s'agit d'une liste en utilisant isinstance(lst[i], list).
    for i in range(len(liste)):

        if isinstance(liste[i], liste):
            #Pour chaque paire d'éléments adjacents elle calcule leur produit et vérifie s'il est présent dans la sous-liste en utilisant any()
            if any(liste[i][j] * liste[i][j+1] in liste[i] for j in range(len(liste[i])-1)):
                #Si le produit d'au moins une paire d'éléments adjacents est trouvé dans une sous-liste, la fonction retourne True sinon false
                return True
            
    return False