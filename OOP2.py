import json

with open('cookbook.txt', 'r', encoding='utf8') as file:
    dishes = {}
    for dishes_name in file:
        person_count = int(file.readline())
        ingridients = []

        for i in range(person_count):

            ingridient_name, quantity, measure = file.readline().strip().split(' | ')
            ingridients.append({
                'ingridient_name': ingridient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        dishes[dishes_name.strip()] = ingridients

    with open('result.json', 'w', encoding='utf-8') as outfile:
        json.dump(dishes, outfile, ensure_ascii=False)




