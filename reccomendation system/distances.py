from metal_album_dataset import MetalAlbumDataSet
from math import sqrt

tree_main = {
    'Жанр': ['Жанр','Поджанр'],
    'Вокал': ['Вокальный/Инструментальный','Тип вокала']
}

tree_variants = {
    'Жанр': {'Жанр':[ 'Нью', 'Рэп-метал', 'Рэпкор','Грув','Глэм','Хэви', 'Трэш-метал','Дэт-метал', 'Блэк-метал', 'Прогрессив','Джент'],
        'Поджанр':['Классический', 'Прогрессив', 'Мелодик', 'Технический', 'Симфоник', 'Американский', 'Немецкий']},
    'Вокал': {'Вокальный/Инструментальный':['Вокальный', 'Инструментал'],
    'Тип вокала': ['Экстрим-вокал', 'Чистый вокал', 'Рэп']}
}

def pow_distance(attr_list_1: list, attr_list_2: list, power: int) -> float:
    weights = [1, 1/2000, 1, 1, 1/4000]
    distance = 0
    ind = 0
    for i in attr_list_1:
        distance += pow(abs(attr_list_1[i] - attr_list_2[i]) * weights[ind], power)
        ind += 1
    return pow(distance, 1/power)

def euclidean(leaf_1: dict, leaf_2: dict) -> float:
    return pow_distance(leaf_1['Атрибуты'], leaf_2['Атрибуты'], 2)

def manhattan(leaf_1: dict, leaf_2: dict) -> float:
    return pow_distance(leaf_1['Атрибуты'], leaf_2['Атрибуты'], 1)

def tree_distance(leaf_1: dict, leaf_2: dict) -> float:
    distance = 0
    diff = []
    for node in tree_main:
        for key in tree_main[node]:
            try:
                leaf_1_tree = tree_variants[node][key].index(leaf_1[node].get(key))
                leaf_2_tree = tree_variants[node][key].index(leaf_2[node].get(key))
            except ValueError:
                diff.append(0)
            else:    
                diff.append(abs( leaf_1_tree - leaf_2_tree)/len(tree_variants[node][key]))
                
    weights = [1, 0.4, 0.4, 0.2]
    for i in range(len(diff)):
        distance += diff[i]*weights[i]
    return distance

def combination_distance(leaf_1: dict, leaf_2: dict) -> float:
    tree_dist = tree_distance(leaf_1, leaf_2) * 1.5
    man_dist = euclidean(leaf_1, leaf_2) * 1/3
    euc_dist = manhattan(leaf_1, leaf_2) * 1/3
    return tree_dist + man_dist + euc_dist