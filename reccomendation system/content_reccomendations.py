from dis import dis
from metal_album_dataset import MetalAlbumDataSet
from distances import combination_distance

def seed_recommendation(ds: MetalAlbumDataSet, seed: dict) -> list:
    arr = []
    for object in ds:
        object['Расстояние'] = combination_distance(object, seed)
        arr.append(object)
    arr.sort(key=lambda object: object['Расстояние'])
    return arr

def likes_reccomendation(ds: MetalAlbumDataSet, likes: list):
    arr = []
    for object in ds:
        distance = 0
        for like_object in likes:
            distance += combination_distance(object, like_object)**2
        distance **= 0.5
        object['Расстояние'] = distance
        arr.append(object)
    arr.sort(key=lambda object: object['Расстояние'])
    return arr

def dislikes_reccomendation(ds: MetalAlbumDataSet, dislikes: list, likes: list):
    arr = likes_reccomendation(ds, likes)
    i = 0
    while i < len(arr):
        if arr[i] in dislikes:
            arr.pop(i)
            i -=1
        i += 1
    return arr