def load_cook_book(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break

            person_count = int(file.readline())
            ingredients = []

            for _ in range(person_count):
                ingredient_info = file.readline().strip().split(' | ')
                ingredient = {
                    'ingredient': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients
            file.readline()  # Пустая строка между блюдами

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count

    return shop_list


cook_book = load_cook_book('cookbook.txt')
result = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(result)