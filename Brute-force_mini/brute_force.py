import itertools

# la liste de caractères à utiliser pour le bruteforce
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# la longueur du mot de passe à bruteforce
length = 6

# le mot de passe à trouver
password = "my_password"

# itération sur toutes les combinaisons possibles de caractères
for guess in itertools.product(charset, repeat=length):
    # concaténer les caractères pour former une chaîne
    guess = "".join(guess)
    # comparer la tentative avec le mot de passe réel
    if guess == password:
        print("Le mot de passe est :", guess)
        break
