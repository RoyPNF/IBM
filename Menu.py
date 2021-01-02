import random

# materials = ["Chicken", "Duck", "Fish", "Pork", "Beef", "lamb"]
#
# for material in range (0,2):
#     print(random.choice(materials))

menu = ["xxx", "yy","zz", "xyz", "xuhgk"]

material_bought = input("Please enter what material you bought:\n")
for dishes in menu:
    if material_bought in dishes:
        print(dishes)
