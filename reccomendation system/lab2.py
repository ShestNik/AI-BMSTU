from distances import euclidean, manhattan, tree_distance, combination_distance
from metal_album_dataset import MetalAlbumDataSet, attributes_list

if __name__ == "__main__":
    ds = MetalAlbumDataSet(fname='documents/dataset.txt')
    for i in range(int(len(ds)/2)):
        for j in range(i + 1, len(ds)):
            print('======================')
            print(ds[i]['Название'],';',ds[j]['Название'])
            print(f"Евклидово расстояние: {euclidean(ds[i], ds[j])}")
            print(f'Манхеттеновское расстояние: {manhattan(ds[i], ds[j])}') 
            print(f'Расстояние по дереву: {tree_distance(ds[i], ds[j])}')
            print(f'Линейная комбинация: {combination_distance(ds[i], ds[j])}')
    '''
    n = len(ds)
    for i in range(int(len(attributes_list)/2)):
        for j in range(i + 1, len(attributes_list)):

            r = 0
            for object in ds:
                z_x = object['Атрибуты'][attributes_list[i]]
                z_y = object['Атрибуты'][attributes_list[j]]
                r += z_x * z_y
            r /= n - 1
    '''