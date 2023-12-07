# Vnořená smyčka je smyčka uvnitř jiné smyčky. Vnitřní smyčka se provede jednou při každé iteraci vnější smyčky.


adjectives = ["black", "stylish", "expensive"]
clothes = ["jacket", "shirt", "boots"]

for x in adjectives:
  for y in clothes:
    print(x, y)

# Výstup:
#
# black jacket
# black shirt
# black boots
# stylish jacket
# stylish shirt
# stylish boots
# expensive jacket
# expensive shirt
# expensive boots


# TODO: Vytvořte koordináty prvků

coordinates = [1, 2, 3]

for coordinate1 in coordinates:
    # TODO: zde použijte vnořenou smyčku.
        print(f'{coordinate1} x {coordinate2}')