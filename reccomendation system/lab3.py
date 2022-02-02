from content_reccomendations import seed_recommendation, likes_reccomendation, dislikes_reccomendation
from metal_album_dataset import MetalAlbumDataSet
from user_profile import UserProfile

if __name__ == '__main__':
    ds = MetalAlbumDataSet(fname='documents/dataset.txt')
    profile = UserProfile()
    print(ds)
    id = int(input('Введите id затравки '))
    recommendation = seed_recommendation(ds, ds[id-1])
    seed = MetalAlbumDataSet(ds=recommendation, show_number=10)
    print("\n===================\nСписок рекомендаций\n===================\n")
    print(seed)
    print()
    likes = []
    dislikes = []
    flag =  'Д'
    while flag == 'Д' or flag == 'Y':
        id = map(int, input('Введите id лайков через пробел ').split())
        profile.likes = list(map(lambda id: ds[id-1],id))
        print("\n===================\nСписок рекомендаций\n===================\n")
        print()
        id = map(int, input('Введите id дизлайков через пробел ').split())
        profile.dislikes = list(map(lambda id: ds[id-1],id))
        recommendation = MetalAlbumDataSet(ds=dislikes_reccomendation(ds, profile.dislikes, profile.likes), show_number=10)
        print("\n===================\nСписок рекомендаций\n===================\n")
        print(recommendation)
        flag = input("Продолжить? Д/н ")