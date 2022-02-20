def open_file():
    with open('recipes.txt') as file:
        cook_book = {}
        for line in file:
            line = line.strip()
            cook_book.update({line: []})
            k = int(file.readline().strip())
            for _ in range(k):
                lst = file.readline().strip().split(' | ')
                dict = {'ingredient_name': lst[0], 'quantity': lst[1], 'measure': lst[2]}
                cook_book[line].append(dict)
            file.readline()
    print(cook_book)

cook_book = {
   'Омлет': [
     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
     ],
   'Утка по-пекински': [
     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
     ],
   'Запеченный картофель': [
     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
     ]
   }

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish in dishes:
        # if i in cook_book:
        for i in cook_book[dish]:
            if i['ingredient_name'] in shopping_list.keys():
                shopping_list[i['ingredient_name']]['quantity'] += i['quantity'] * person_count
            else:
                shopping_list[i['ingredient_name']] = {}
                shopping_list[i['ingredient_name']]['measure'] = i['measure']
                shopping_list[i['ingredient_name']]['quantity'] = i['quantity'] * person_count

    print(shopping_list)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 1)


# def amount_str(file_name):
#     file_path = os.path.abspath(os.path.join(file_name))
#     with open(file_path, encoding='utf8') as file_work:
#         return len(file_work.readlines())
#
#
# def read_file(file_name):
#     file_path = os.path.abspath(os.path.join(file_name))
#     with open(file_path, encoding='utf8') as file_work:
#         return file_work.read()


# doc_list = []
# dict = {}
# sort = {}
#
# doc_list.append(sort.keys())
# file_name = ['1.txt', '2.txt', '3.txt']
# for file in file_name:
#     dict.setdefault(file, amount_str(file))
# sort = {k: dict[k] for k in sorted(dict, key=dict.get, reverse=False)}
# file_for_write = []
# file_for_write.extend(sort.keys())
#
# print(sort)
#
# for file in file_for_write:
#     text = read_file(file)
#     text_2 = amount_str(file)
#     with open('15.txt', 'a') as f:
#         f.write(f'{file}' '\n' f'{text_2}' '\n' f'{text}' '\n')