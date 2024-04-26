"""
Ce script permet l'échange de dollars en gourdes et gourdes en dollars.
"""

import os


def clear_screen():
    """
    Efface l'écran.

    Cette fonction efface l'écran ou effectue une opération similaire,
    selon les besoins de  l'application.
    """
    os.system("cls" if os.name == 'nt' else 'clear')


def menu():
    """
    function of menu
    """
    print("\n" * 2)
    print("\x1b[6;32;25m" + "\t" * 1 +
              " •••••••Bienvenue ! dans le programme •••••••" +
              "\x1b[0m")
    print("\n" * 2)
    print("\t" * 2, "1. Convertir gourdes en dollar")
    print("\t" * 2, "2. Convertir dollar en gourdes")
    print("\t" * 2, "3. Quitter")
    print()
    choice = int(input("\t" * 2 + "Faites un choix (1-3) : "))
    return choice


def error_choice():
    """
    ...
    """
    clear_screen()
    print()
    print("\t" * 1,
                              "Votre saisie doit être un nombre valide")
    input("\t" * 1 +
                              "Presser Entrée/Enter pour continuer")
    

def main():
    """
    Main function.

    This is the main entry point of the script.
    """
    while True:
        try:
            clear_screen()
            choice = menu()
            if 1 <= choice <= 3:
                while choice != 3:
                    if choice == 1:
                        clear_screen()
                        print("\n" * 2)
                        somme2 = input("\t" * 2 +
                                   "Entrez le montant en gourdes : ")

                        try:
                            somme = float(somme2)
                            clear_screen()
                            print()
                            print("\t" * 3, somme, " gourdes")
                            print()
                            print("\t" * 2, "Équivaut à :")
                            print()
                            somme_dollar = somme / 5
                            print("\t" * 3, somme_dollar, " dollars")
                            print('\n' * 2)
                            input("\t" * 1 +
                              "Presser Entrée/Enter pour continuer")
                            clear_screen()
                            break

                        except ValueError:
                            error_choice
                            continue

                    if choice == 2:
                        clear_screen()
                        print("\n" * 2)
                        somme1 = input("\t" * 2 +
                                   "Entre le montant en dollar : ")
                        try:
                            somme = float(somme1)
                            clear_screen()
                            print("\n" * 2)
                            print("\t" * 3, somme, "dollars")
                            somme_gourdes = somme * 5
                            print()
                            print("\t" * 2, "Équivaut à :")
                            print()
                            print("\t" * 3, somme_gourdes, "gourdes")
                            print('\n' * 2)
                            input("\t" * 1 +
                              "Presser Entrée/Enter pour continuer")
                            clear_screen()
                            break

                        except ValueError:
                           error_choice()
                           continue

                if choice == 3:
                    clear_screen()
                    print("\n" * 2)
                    print("\t" * 2, "Vous quittez le programme.")
                    break

            else:
                clear_screen()
                print("\t" * 1, "Invalide. Veuillez choisir entre 1 à 3")
                input("\t" * 1 +
                  "Presser Entrée/Enter pour continuer")
                continue

        except ValueError:
            error_choice()
            continue


# Main
if __name__ == "__main__":
    main()
