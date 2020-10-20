#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    userInput = float(input("Entrez n'importe quel nombre: "))
    userInput = abs(userInput)
    return userInput


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    names = []
    for i in prefixes:
        names.append(i+suffixes)
    return names


def prime_integer_summation() -> int:
    prime_number_list = [2]
    for i in range(100):
        isprime = True
        for n in range(len(prime_number_list)):
            if i % n != 0:
                isprime = False
                break
        if isprime:                    
            prime_number_list.append(i)
            print(prime_number_list)
    return sum(prime_number_list)


def factorial(number: int) -> int:
    value = 1
    for i in range(1, number+1):
        value = i* value
    return value


def use_continue() -> None:
    for i in range(1,11):
        if i !=5:
            print(i)
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
