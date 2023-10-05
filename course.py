panier = []

while True:
    print("Menu :")
    print("1. Ajouter")
    print("2. Retirer")
    print("3. Afficher")
    print("4. Vider")
    print("5. Quitter")

    choix = input("Choisissez une option (1/2/3/4/5) : ")

    if choix == "1":
        # Code pour l'option 1
        element = input ("Entre le nom d'un élément à ajouter : ")
        panier.append(element)
        
        
    elif choix == "2":
        element = input("Entrez l'élément à retirer de la liste : ")
        if element in panier:
            panier.remove(element)  # Retirer l'élément de la liste s'il existe
            print(f"{element} a été retiré de la liste de courses.")
        else:
            print(f"{element} n'était pas dans la liste de courses.")
            
    elif choix == "3":
        # Code pour l'option 3
        print("Liste de courses :")
        for item in panier:
            print(item)
            
    elif choix == "4":
        panier.clear()  # Vider la liste de courses
        print("La liste de courses a été vidée.")
    elif choix == "5":
        # Code pour l'option 5 (Quitter)
        print("Vous avez choisi l'option 5. Au revoir !")
        break  # Sort de la boucle pour terminer le programme
    else:
        print("Choix invalide. Veuillez sélectionner une option valide (1/2/3/4/5).")
