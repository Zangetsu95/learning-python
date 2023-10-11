import random

"""
Règles du jeu
Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.

Le jeu comporte deux joueurs : vous et un ennemi.

Vous commencez tous les deux avec 50 points de vie.

Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.

L'ennemi ne dispose d'aucune potion.

Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.

Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.

L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.

Lorsque vous utilisez une potion, vous passez le prochain tour.

"""
# Player
player_life = 50
player_attack = random.randint(5, 10)
heal = 3

# Ennemi
ennemy_life = 50
ennemy_attack = random.randint(5, 15)

print("-----------------------------------------------")
print("Bienvenue dans le jeu du RPG !")
print(f"Vous avez {player_life} points de vie 🐱‍🏍")
print(f"Votre opposant a {ennemy_life} points de vie 👺")

while player_life > 0 and ennemy_life > 0:
    print("-----------------------------------------------")
    choice = int(input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "))

    try:
        if choice < 1 or choice > 2:
            print("Veuillez entrer 1 pour attaquer ou 2 pour utiliser une potion.")
            continue
    except ValueError:
        print("Veuillez entrer un chiffre valide !")
        continue

    if choice == 1:
        ennemy_damage = random.randint(5, 10)
        ennemy_life -= ennemy_damage
        print(f"L'ennemi a perdu {ennemy_damage} points de vie. Il lui en reste {ennemy_life}.")

        player_damage = random.randint(5, 15)
        player_life -= player_damage
        print(f"Vous avez perdu {player_damage} points de vie. Il vous en reste {player_life}.")

    elif choice == 2:
        if heal > 0:
            heal_amount = random.randint(15, 50)
            player_life += heal_amount
            heal -= 1
            print(f"Vous avez utilisé une potion et récupéré {heal_amount} points de vie 💗. Il vous reste {heal} potions 💕.")

            ennemy_damage = random.randint(5, 15)
            player_life -= ennemy_damage
            print(f"L'ennemi vous a attaqué et vous a fait perdre {ennemy_damage} points de vie. Il vous en reste {player_life}.")

            if heal == 0:
                print("Vous n'avez plus de potions.")
        else:
            print("Vous n'avez plus de potions.")

if player_life <= 0:
    print("Vous avez perdu honnorable guerrier !")
else:
    print("Félicitations ! Vous avez battu l'ennemi.")
   
    
