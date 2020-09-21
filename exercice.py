#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    userInput = float(input("Entrez n'importe quel nombre"))
    userInput = abs(userInput)
    return userInput


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    names = []
    for i in prefixes:
        names.append(i+suffixes)
    return names


def prime_integer_summation() -> int:
    for i in range(1,100):
        number = 0
        while number <10:
            number+=1
            if i%number != 0:
                number += 1
            elif i%number:
                break
    return 0


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
