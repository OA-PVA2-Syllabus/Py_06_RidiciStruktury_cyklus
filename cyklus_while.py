#Smyčka while je do jisté míry podobná příkazu if: provede nějaký kód, pokud je nějaká podmínka True.
# Hlavní rozdíl spočívá v tom, že bude pokračovat ve vykonávání odsazeného kódu tak dlouho, dokud bude podmínka True.
# Pokud je výraz False, smyčka se ukončí.

square = 1  # Proměnná zavedená pro sledování iterací

while square <= 10:
    print(square)    # Tento kód se provede 10krát
    square += 1      # Tento kód se provede 10krát

print("Finished")  # Tento kód se provede jednou

square = 0
number = 1


# TODO: Vytiskněte všechny druhé mocniny od 1 do 81.
# Zde použijte příkaz while a podmínku.

    square = number ** 2
    print(square)
    number += 1