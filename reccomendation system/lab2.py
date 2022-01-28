from distances import euclidean, manhattan, tree_distance, combination_distance
from metal_album_dataset import MetalAlbumDataSet

if __name__ == "__main__":
    ds = MetalAlbumDataSet('documents/dataset.txt')
    for i in ds:
        for j in ds:
            print('======================')
            print(i['Название'],j['Название'])
            print(euclidean(i, j))
            print(manhattan(i, j))
            print(tree_distance(i, j))
            print(combination_distance(i,j))