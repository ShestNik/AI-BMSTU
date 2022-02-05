from user_profile import UserProfile
from metal_album_dataset import MetalAlbumDataSet
from datetime import datetime

attributes_list = [
    'Исполнитель',
    'Год',
    'Оригинальный/Кавер',
    'Формат',
    'Длительность'
]

def search(search_params: dict, ds: MetalAlbumDataSet, profile: UserProfile):
    error = ''
    filtered_ds = ds
    for key in search_params:
        if key == 'Название':
            filter_type = search_params[key]['Тип фильтра']
            value =  search_params[key]['Значение']
            if filter_type == '=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object[key] == value))
            elif filter_type == 'содержит':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: value in object[key]))                
            else:
                error = 'Неправильный тип фильтра'
                break
        if key == 'Исполнитель':
            filter_type = search_params[key]['Тип фильтра']
            value =  search_params[key]['Значение']
            if filter_type == '=':
                value = MetalAlbumDataSet.convert_band(value)
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
            elif filter_type == 'содержит':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: value in MetalAlbumDataSet.convert_band_reverse(object['Атрибуты'][key])))                
            else:
                error = 'Неправильный тип фильтра'
                break
        if key == 'Год':
            filter_type = search_params[key]['Тип фильтра']
            value =  search_params[key]['Значение']
            value = MetalAlbumDataSet.convert_year(value)
            if filter_type == '=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
            elif filter_type == '>':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] > value))  
            elif filter_type == '<':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] < value))
            elif filter_type == '>=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] >= value))
            elif filter_type == '<=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] <= value))          
            else:
                error = 'Неправильный тип фильтра'
                break
        if key == 'Оригинальный/Кавер':
            filter_type = search_params[key]['Тип фильтра']
            value =  search_params[key]['Значение']
            value = MetalAlbumDataSet.convert_original(value)
            if filter_type == '=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
            else:
                error = 'Неправильный тип фильтра'
                break
        if key == 'Формат':
            filter_type = search_params[key]['Тип фильтра']
            value =  search_params[key]['Значение']
            value = MetalAlbumDataSet.convert_format(value)
            if filter_type == '=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
            else:
                error = 'Неправильный тип фильтра'
                break
        if key == 'Длительность':
            filter_type = search_params[key]['Тип фильтра']
            value =  search_params[key]['Значение']
            value = MetalAlbumDataSet.convert_duration(value)
            if filter_type == '=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
            elif filter_type == '>':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] > value))  
            elif filter_type == '<':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] < value))
            elif filter_type == '>=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] >= value))
            elif filter_type == '<=':
                filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] <= value))          
            else:
                error = 'Неправильный тип фильтра'
                break
    return error, filtered_ds

class Search:
    query_history = []
    search_history = []

    def search(self, search_params: dict, ds: MetalAlbumDataSet, profile: UserProfile):
        error = ''
        filtered_ds = ds
        for key in search_params:
            if key == 'Название':
                filter_type = search_params[key]['Тип фильтра']
                value =  search_params[key]['Значение']
                if filter_type == '=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object[key] == value))
                elif filter_type == 'содержит':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: value in object[key]))                
                else:
                    error = 'Неправильный тип фильтра'
                    break
            if key == 'Исполнитель':
                filter_type = search_params[key]['Тип фильтра']
                value =  search_params[key]['Значение']
                if filter_type == '=':
                    value = MetalAlbumDataSet.convert_band(value)
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
                elif filter_type == 'содержит':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: value in MetalAlbumDataSet.convert_band_reverse(object['Атрибуты'][key])))                
                else:
                    error = 'Неправильный тип фильтра'
                    break
            if key == 'Год':
                filter_type = search_params[key]['Тип фильтра']
                value =  search_params[key]['Значение']
                value = MetalAlbumDataSet.convert_year(value)
                if filter_type == '=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
                elif filter_type == '>':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] > value))  
                elif filter_type == '<':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] < value))
                elif filter_type == '>=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] >= value))
                elif filter_type == '<=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] <= value))          
                else:
                    error = 'Неправильный тип фильтра'
                    break
            if key == 'Оригинальный/Кавер':
                filter_type = search_params[key]['Тип фильтра']
                value =  search_params[key]['Значение']
                value = MetalAlbumDataSet.convert_original(value)
                if filter_type == '=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
                else:
                    error = 'Неправильный тип фильтра'
                    break
            if key == 'Формат':
                filter_type = search_params[key]['Тип фильтра']
                value =  search_params[key]['Значение']
                value = MetalAlbumDataSet.convert_format(value)
                if filter_type == '=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
                else:
                    error = 'Неправильный тип фильтра'
                    break
            if key == 'Длительность':
                filter_type = search_params[key]['Тип фильтра']
                value =  search_params[key]['Значение']
                value = MetalAlbumDataSet.convert_duration(value)
                if filter_type == '=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] == value))
                elif filter_type == '>':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] > value))  
                elif filter_type == '<':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] < value))
                elif filter_type == '>=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] >= value))
                elif filter_type == '<=':
                    filtered_ds = MetalAlbumDataSet(ds=filtered_ds.filter(lambda object: object['Атрибуты'][key] <= value))          
                else:
                    error = 'Неправильный тип фильтра'
                    break
        self.query_history.append(search_params.copy())
        self.search_history.append(filtered_ds)
        return error, filtered_ds

    def print_history(self) -> str:
        res = ""
        i = 0
        for i in range(len(self.query_history)):
            query = self.query_history[i]
            search = self.search_history[i]
            res += f"\n{i} запрос. Строка запроса: \n"
            for key in query:
                res += f"{key} {query[key]['Тип фильтра']} {query[key]['Значение']}\n"
            res += "\nСодержимое запроса:\n"
            res += str(search)
        return res

    def __getitem__(self, key: int):
        return self.search_history[key]
        