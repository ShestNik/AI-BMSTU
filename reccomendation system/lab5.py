from content_reccomendations import seed_recommendation, dislikes_reccomendation
from metal_album_dataset import MetalAlbumDataSet
from user_profile import UserProfile
from search import search
import re

attributes_list = [
    'Название',
    'Исполнитель',
    'Год',
    'Оригинальный/Кавер',
    'Формат',
    'Длительность'
]
menu = '\n0 - выйти\n1 - поиск\n2 - лайк\n3 - дизлайк\n4 - выдать рекомендацию\n\nВведите номер пункта меню: '
filter_menu = f'\nВведите фильтр по принципу: имя_атрибута = значение по одному\nСписок атрибутов: {attributes_list}\nДополнительные опции у атрибутов год,длительность: ">", "<", ">=", "<="\nДополнительная опция у исполнителя и названия: "содержит"\nФормат длительности ЧЧ:ММ:СС либо ММ:СС либо ММ\nДля выхода введите пустую строку: '

def like(profile: UserProfile, ds: MetalAlbumDataSet):
    id = map(int, input('Введите id лайков через пробел ').split())
    profile.likes = list(map(lambda id: ds[id-1],id))
    return profile

def dislike(profile: UserProfile, ds: MetalAlbumDataSet):
    id = map(int, input('Введите id дизлайков через пробел ').split())
    profile.dislikes = list(map(lambda id: ds[id-1],id))
    return profile

def reccomendation(profile: UserProfile, ds: MetalAlbumDataSet):
    return MetalAlbumDataSet(ds=dislikes_reccomendation(ds, profile.dislikes, profile.likes))

def search_input(ds: MetalAlbumDataSet, profile: UserProfile):
    search_params_dict = {}
    flag = 1
    full_string = ''
    while flag:
        parse_string = input(filter_menu)
        pattern = r'(\S+) (=|<|>|<=|>=|содержит) (\S+)'
        if parse_string:
            match = re.fullmatch(pattern, parse_string)
            if match:
                match = re.findall(pattern, parse_string)[0]
                #print(match)
                search_params_dict[match[0]] = {'Тип фильтра': match[1], 'Значение': match[2]}
                full_string += f"{parse_string}\n"
            else:
                print('\nВы ввели неверное выражение. Попробуйте еще раз.\n')
        else:    
            flag = 0
        print(f'\nТекущий запрос:\n{full_string}')
    print(f'\nИтоговый запрос:\n{full_string}')
    return search(search_params_dict, ds, profile)

if __name__ == '__main__':
    ds = MetalAlbumDataSet(fname='documents/dataset.txt')
    profile = UserProfile()
    print(ds)
    likes = []
    dislikes = []
    flag = 1
    while flag != 0:
        flag = int(input(menu))
        if flag == 1:
            error, searched_ds = search_input(ds, profile)
            if not error and searched_ds:
                print('Результат поиска: \n')
                print(searched_ds)
            elif not searched_ds:
                print('Ничего не найдено. Однако мы рекомендуем:\n')
                print(reccomendation(profile, ds))
            else:
                print(error)
        elif flag == 2:
            profile = like(profile, ds)
        elif flag == 3:
            profile = dislike(profile, ds)
        elif flag == 4:
            print(reccomendation(profile, ds))
        elif flag == 0:
            pass
        else:
            print('Введите целое число от 0 до 4')
        