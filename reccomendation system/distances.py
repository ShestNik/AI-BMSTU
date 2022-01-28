from metal_album_dataset import MetalAlbumDataSet
from math import sqrt

tree_main = {
    'Жанр': ['Жанр','Поджанр'],
    'Вокал': ['Вокальный/Инструментальный','Тип вокала']
}

def pow_distance(attr_list_1, attr_list_2, power):
    weights = [1, 1/2000, 1, 1, 1/4000]
    distance = 0
    ind = 0
    for i in attr_list_1:
        distance += pow(abs(attr_list_1[i] - attr_list_2[i]) * weights[ind], power)
        ind += 1
    return pow(distance, 1/power)

def euclidean(leaf_1, leaf_2):
    return pow_distance(leaf_1['Атрибуты'], leaf_2['Атрибуты'], 2)

def manhattan(leaf_1, leaf_2):
    return pow_distance(leaf_1['Атрибуты'], leaf_2['Атрибуты'], 1)

def tree_distance(leaf_1, leaf_2):
    distance = 0
    diff = []
    for node in tree_main:
        for key in tree_main[node]:
            diff.append(0 if leaf_1[node].get(key) == leaf_2[node].get(key) else 1)
    weights = [0.5, 0.3, 0.2, 0.1]
    for i in range(len(diff)):
        distance += diff[i]*weights[i]
    return distance

def combination_distance(leaf_1, leaf_2):
    tree_dist = tree_distance(leaf_1, leaf_2) * 1.5
    man_dist = euclidean(leaf_1, leaf_2)
    euc_dist = manhattan(leaf_1, leaf_2)
    return tree_dist + man_dist + euc_dist