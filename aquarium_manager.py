# Objetivo: Colocar todos os animais do tipo fish
# no tanque 50

import json

o = open('aquarium.json', encoding='utf8')  
dados_aquarium = json.load(o)
animals = dados_aquarium['dados']

# def verify_fish(animal):
    
#     if animal["type"] == "fish":
#         return True
#     return False

# Usando a função lambda
animals_fish = list(filter(lambda animal: (animal["type"] == "fish"),animals))

# Pegando só os nomes dos peixes

def animal_name(animal):
    return animal["name"]

animals_fish_name = list(map(animal_name,animals_fish))

# Mudando o tanque

def assign_to_tank(animals,name_select,new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in name_select:
            animal["tank_number"] = new_tank_number
        return animal
    return list(map(change_tank_number,animals))

new_aquarium = assign_to_tank(animals,animals_fish_name,50)
print(new_aquarium)