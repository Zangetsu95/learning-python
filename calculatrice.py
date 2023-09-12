number_1 = float(input('choisisez votre premier chiffre'))
number_2 = float(input('choisisez votre deuxième chiffre'))

operator = input('Choisissez un opérateur (+, -, *, /) : ')

if operator == '+':
    result = number_1 + number_2
elif operator == '-':
    result = number_1 - number_2
elif operator =='*':
    result = number_1  *number_2
elif operator == '/':
    if number_2 == 0:
        print("Erreur : Division par zéro n'est pas autorisée.")
    else:
        result = number_1 / number_2
else:
    print("Opérateur invalide.")

# Affichez le résultat
print(f"Le résultat de {number_1} {operator} {number_2} est égal à {result}")
