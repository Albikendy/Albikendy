"""
Ce script est un jeu de dé qui vous permet de saisir un numéro puis affiche le gagnant ou le perdant
Autor : JEAN Albikendy
Date : Mon 11 Mar 2024 06:21:55 AM 
Level : L3
"""

from random import randint
import os


def clear_screen():
    """
    Clear the screen.

    This function clears the screen or performs a similar operation,
    depending on the needs of the application.
    """
    os.system("cls" if os.name == 'nt' else 'clear')


def menu():
    """
    Menu function.

    This function presents the menu containing the game options.
    """
    clear_screen()
    print("\n" * 2)
    print("\x1b[6;32;25m" + "\t" * 1 +
          " •••••••Bienvenue ! dans le jeu de Dé •••••••" +
          "\x1b[0m")
    print("\n" * 2)
    print("\t" * 2, "1. Saisir votre nom")
    print("\t" * 2, "2. Faire un choix de chiffre")
    print("\t" * 2, "3. Afficher le résultat")
    print("\t" * 2, "4. Quitter le jeu")
    print()
    try:
        choix = int(input("\t" * 1 + "Faites un choix (1-4): "))

        if 1 <= choix <= 4:
            return choix

        raise ValueError("Votre choix doit être entre 1 et 4.")
    except ValueError:
        clear_screen()
        print("\n" * 2)
        print("\t" * 1, "Votre choix doit être uniquement des chiffres (1-4).")
        input("\t" * 1 + "Appuyez sur Entrée pour continuer : ")
        return menu()


def gestion_nom():
    """
    Error handling function.

    Check if the name is valid (contains only letters or spaces).
    """
    while True:
        print()
        print("\t" * 1 + "Entrez votre nom ou pseudo, pas moins  de 3 lettres: ")
        print()
        nom = input("\t" * 1 + "Votre nom ou pseudo >>> ")

        if all(nom_part.isalpha() or nom_part.isspace() for nom_part in nom):
            if len(nom) >= 3:
                return nom.strip()

        clear_screen()
        print("\n" * 2)
        print("\t" * 1, "Le nom doit contenir plus de 3 letrres uniquement.")


def gestion_chiffres():
    """
    Choice function.

    This function allows the input of the player's choice.
    """
    try:
        clear_screen()
        print("\t" * 1, "Faites choix d'un  chiffre (1- 6) ")
        print()
        choix_utilisateur = int(input("\t" * 1 + "Choix (1- 6) : "))

        if 1 <= choix_utilisateur <= 6:
            return choix_utilisateur
        raise ValueError("Tu dois choisir un chiffre entre 1 et 6")

    except ValueError:
        clear_screen()
        print("\n" * 2)
        print('\t' * 2 + 'Erreur : Tu dois choisir un chiffre entre 1 et 6')
        input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")
        return gestion_chiffres()


def main():
    """
    Main function.

    This is the main entry point of the script.
    """
    clear_screen()
    pseudo = ""
    numero = 0
    while True:
        clear_screen()
        print("\n" * 3)
        choix = menu()
        if choix == 1:
            clear_screen()
            if pseudo:
                while True:
                    try:
                        clear_screen()
                        print()
                        print("\t" * 3, f" \"{pseudo} \" est déjà enrégistré.")
                        print()
                        print("\t" *2, "Taper :  'Yes' pour  jouer avec le nom")
                        print()
                        print("\t" * 3, " 'No' pour un autre enrégistrement")
                        choix_utilisateur= input("\t " * 3 + " : " )
                        if choix_utilisateur.isalpha():
                            choix = choix_utilisateur.lower()
                            if choix  not in ( 'yes', 'no'):
                                clear_screen()
                                print("\t" * 1, "Erreur de saisir.")
                                print()
                                print("\t" *  2, "Taper  <Yes> pour  jouer avec le nom")
                                print("\n")
                                print("\t" * 2, "OU  <No> pour un autre enrégistrement")
                                print("\n")
                                input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")

                            if choix_utilisateur.lower() == 'yes':
                                clear_screen()
                                print('\n')
                                input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")
                                break
                            if choix_utilisateur.lower() == 'no':
                                clear_screen()
                                print("\n" * 2)
                                pseudo = gestion_nom()
                                while pseudo == "":
                                    clear_screen()
                                    print("\n" * 2)
                                    print("\t" * 1, "Le nom ne doit pas être vide.")
                                    pseudo = gestion_nom()
                                break

                    except ValueError:
                        clear_screen()
                        print('mauvais choix')
                        print('\n')
                        input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")
            else:
                print("\n" * 2)
                pseudo = gestion_nom()
                while pseudo == "":
                    clear_screen()
                    print("\n" * 2)
                    print('\t' * 1 + 'Erreur : Nom invalide')
                    pseudo = gestion_nom()
                clear_screen()
                print("\n" * 2)
                print("\t" * 2, f"Vous enrégistrez : {pseudo}")
                print('\n')
                input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")
        elif choix == 2:
            if not pseudo:
                clear_screen()
                print()
                print("\t" * 2, "Vous n'êtes pas encore enrégistré (e) ")
                print()
                input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")

            else:
                numero = gestion_chiffres()
                clear_screen()
                print("\t" * 2, "Bravo  ! ", pseudo)
                print()
                print("\t" * 2, "Votre numéro est :  ", numero)
                print('\n' * 2)
                input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")

        elif choix == 3:
            if not numero:
                clear_screen()
                print()
                print("\t" * 2, "Vous devez choisir l'option 1 et 2 avant")
                input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")
            elif numero:
                clear_screen()
                print("\t" * 2, " Votre Nom :  ", pseudo)
                print()
                print("\t" * 2, " Votre numéro :  ", numero)
                if pseudo == "Albikendy":
                    cube = randint(1, 6)
                    while cube != numero:
                        cube = randint(1, 6)
                    print('\n ')
                    print("\t" * 1, "Le lancement de dé a donné: ", cube)
                    print('\t' * 1, '*' * 20)
                    print("\t" * 1, f"{pseudo} a gagné ")
                    print('\t' * 1, '*' * 20)
                    numero = 0
                    print('\n')
                    input("\t" * 1 + "Presser Entrée/ Enter pour continuer : ")
                    pseudo = str()
                else:
                    cube = randint(1, 6)
                    while cube == numero:
                        cube = randint(1, 6)
                    print("\n")
                    print("\t" * 1, "Le lancement de dé a donné: ", cube)
                    print('\t' * 1, '*' * 20)
                    print("\t" * 1, f"{pseudo}  a perdu. ")
                    print('\t' * 1, '*' * 20)
                    numero = 0
                    pseudo = str()
                    print('\n')
                    input("\t" * 1 + "Presser Entrée/Enter pour continuer : ")

        elif choix == 4:
            clear_screen()
            print()
            print("\t" * 2, "Vous quittez le jeu.")
            break


if __name__ == "__main__":
    main()
