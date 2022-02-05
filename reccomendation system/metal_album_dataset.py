from typing import cast
from datetime import datetime
from math import inf

vocal_variants = [
    ['Вокальный', 'Инструментал'],
    ['Экстрим-вокал', 'Чистый вокал', 'Рэп']
]
genre_variants = [
    ['Глэм','Хэви', 'Грув','Трэш-метал', 'Дэт-метал', 'Блэк-метал', 'Нью', 'Рэпкор','Рэп-метал', 'Прогрессив','Джент'],
    ['Классический', 'Прогрессив', 'Мелодик', 'Технический', 'Симфоник', 'Американский', 'Немецкий']
]
band_variants = [
    'Skid Row', 'Black Sabbath',  'Pantera', 'Sodom','Metallica', 'Megadeth', 'Children Of Bodom', 'Death', 'Dimmu Borgir',  'Slipknot', 'Fever 333'
]
format_variants = ['Альбом', 'Мини-альбом', 'Сингл']

tree_vocal = [
    'Вокальный/Инструментальный',
    'Тип вокала'
]
tree_genre = [
    'Жанр',
    'Поджанр'
]
attributes_list = [
    'Исполнитель',
    'Год',
    'Оригинальный/Кавер',
    'Формат',
    'Длительность'
]

class MetalAlbumDataSet:
    attributes = attributes_list

    dataset = []

    show_number = inf

    def __init__(self, fname=None, ds=None, show_number = -1):
        if ds != None:
            self.dataset = ds
        else:
            self.read_data(fname)
        if show_number != -1:
            self.show_number = show_number
            

    def read_data(self, fname: str):
        data = []
        id = 1
        with open(fname, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                attr_str, vocal_str, genre_str = line[:-1].split('|')
                attr_str = attr_str.split(';')
                attr_converted = self.convert_attributes(attr_str)
                attrs = dict(zip(self.attributes,attr_converted))
                vocal = dict(zip(tree_vocal,vocal_str.split(';')))
                genre = dict(zip(tree_genre,genre_str.split(';')))
                data.append({'id': id, 'Название': attr_str[0],'Атрибуты': attrs, 'Вокал':vocal, 'Жанр':genre})
                id += 1
        self.dataset = data
    
    def convert_attributes(self, attrs: list):
        attributes = [
            band_variants.index(attrs[1])/len(band_variants),
            int(attrs[2]),
            1 if attrs[3] == 'Оригинальный' else 0,
            format_variants.index(attrs[4])/len(format_variants),
            self.convert_duration(attrs[5])
        ]
        return attributes
    
    @staticmethod
    def convert_band(band: str):
        return band_variants.index(band)/len(band_variants)

    @staticmethod
    def convert_band_reverse(band: int):
        return  band_variants[int(band*len(band_variants))]

    @staticmethod
    def convert_original(is_original: str):
        return 1 if is_original == 'Оригинальный' else 0

    @staticmethod
    def convert_format(format: int):
        return format_variants.index(format)/len(format_variants)
    
    @staticmethod
    def convert_duration(duration: str):
        n = duration.count(':')
        if n == 0:
            pattern = '%M'
        elif n == 1:
            pattern = '%M:%S'
        else:
            pattern = '%H:%M:%S'
        duration = datetime.strptime(duration, pattern)
        duration = (duration-datetime(1900,1,1)).total_seconds()
        return  duration

    @staticmethod
    def convert_year(year: str):
        return int(year)

    @staticmethod
    def convert_attributes_reverse(attrs: list):
        attrs = [
            band_variants[int(attrs['Исполнитель']*len(band_variants))],
            attrs['Год'],
            'Оригинальный' if attrs['Оригинальный/Кавер'] == 1 else 'Кавер',
            format_variants[int(attrs['Формат']* len(format_variants))],
            datetime.utcfromtimestamp(attrs['Длительность']).strftime('%H:%M:%S')
        ]
        attrs = dict(zip(attributes_list,attrs))
        return attrs
    
    def filter(self, func):
        return [object for object in self.dataset if func(object)]

    def __getitem__(self, key: int):
        return self.dataset[key]
    
    def __str__(self):
        res = ""
        i = 0
        for object in self.dataset:
            attrs = self.convert_attributes_reverse(object['Атрибуты'])
            string = f"id: {object['id']}, название: {object['Название']}, исполнитель: {attrs['Исполнитель']}, год выхода: {attrs['Год']}, длительность:  {attrs['Длительность']}"
            if i >= self.show_number:
                break
            i += 1
            #for key in object:
            #    if key != 'Атрибуты':
            #        string += f"{key}: {object[key]}; "
            #    else:
            #        string += f"Атрибуты: {attrs}; "
            res += f"{string}\n"
        return res
    
    def __len__(self):
        return len(self.dataset)

if __name__ == "__main__":
    ds = MetalAlbumDataSet('documents/dataset.txt')
    print(len(ds))