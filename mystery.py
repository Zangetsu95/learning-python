import random

# Génération du nombre mystère
nombre_mystere = random.randint(0, 100)

# Nombre d'essais
tentatives_restantes = 5

print("Bienvenue dans le jeu du nombre mystère !")
print(f"Vous avez {tentatives_restantes} essais pour trouver le nombre mystère entre 0 et 100.")

while tentatives_restantes > 0:
    try:
        # Demande à l'utilisateur de deviner le nombre
        guess = int(input("Devinez le nombre : "))
        
        if guess < 0 or guess > 100:
            print("Veuillez entrer un nombre entre 0 et 100.")
            continue  # Redémarrez la boucle pour une nouvelle tentative.

    except ValueError:
        print("Veuillez entrer un chiffre valide !")
        continue  # Redémarrez la boucle pour une nouvelle tentative.

    # Vérification de la proposition de l'utilisateur
    if guess < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    elif guess > nombre_mystere:
        print("Le nombre mystère est plus petit.")
    else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère en {5 - tentatives_restantes + 1} essais.")
        break  # Sortir de la boucle si le nombre a été trouvé

    tentatives_restantes -= 1
    if tentatives_restantes > 0:
        print(f"Il vous reste {tentatives_restantes} essais.")

if tentatives_restantes == 0:
    print(f"Dommage, vous avez épuisé vos {5} essais. Le nombre mystère était {nombre_mystere}.")
