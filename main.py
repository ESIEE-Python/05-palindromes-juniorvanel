#### Fonction secondaire

"""
une fonction qui permet de verifier si une chaine de caractère est un palindromes ou pas
"""
def ispalindrome(p):
    """
    Cette fonction vérifie si la chaîne obtenue est un palindrome.
    Elle normalise la chaîne, supprime les accents et les caractères non alphanumériques,
    puis vérifie si la chaîne est identique lorsqu'elle est lue dans les deux sens.
    """
    p = p.lower()
    table = str.maketrans("àâäéèêëîïôöùûüÿç", "aaaeeeeiioouuuyc")
    p = p.translate(table)
    p = "n".join(c for c in p if c.isalnum())
    return p == p[::-1]

#### Fonction principale
def main():
    """
    Fonction principale qui teste plusieurs chaînes de caractères
    pour vérifier si elles sont des palindromes.
    """
    for s in ["radar", "kayak", "lvel", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
