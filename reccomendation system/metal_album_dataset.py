from typing import cast
from datetime import datetime

vocal_variants = [
    ['Вокальный', 'Инструментал'],
    ['Экстрим-вокал', 'Чистый вокал', 'Рэп']
]
genre_variants = [
    ['Глэм','Хэви', 'Грув','Трэш-метал','Дэт-метал', 'Блэк-метал', 'Нью', 'Рэпкор','Рэп-метал', 'Прогрессив','Джент'],
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

class MetalAlbumDataSet:
    attributes = [
        'Исполнитель',
        'Год',
        'Оригинальный/Кавер',
        'Формат',
        'Длительность'
    ]


    dataset = []

    def __init__(self, fname: str):
        self.read_data(fname)

    def read_data(self, fname: str):
        data = []
        with open(fname, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                attr_str, vocal_str, genre_str = line[:-1].split('|')
                attr_str = attr_str.split(';')
                attr_converted = self.__convert_attributes(attr_str)
                attrs = dict(zip(self.attributes,attr_converted))
                vocal = dict(zip(tree_vocal,vocal_str.split(';')))
                genre = dict(zip(tree_genre,genre_str.split(';')))
                data.append({'Название': attr_str[0],'Атрибуты': attrs, 'Вокал':vocal, 'Жанр':genre})
        self.dataset = data
    
    def __convert_attributes(self, attrs: list):
        n = attrs[5].count(':')
        attributes = [
            band_variants.index(attrs[1])/len(band_variants),
            int(attrs[2]),
            1 if attrs[3] == 'Оригинальный' else 0,
            format_variants.index(attrs[4])/len(format_variants),
            (datetime.strptime(attrs[5], '%M:%S') if n == 1 else datetime.strptime(attrs[5], '%H:%M:%S'))
        ]
        attributes[4] = (attributes[4]-datetime(1900,1,1)).total_seconds()
        return attributes
    
    def __getitem__(self, key: int):
        return self.dataset[key]

if __name__ == "__main__":
    ds = MetalAlbumDataSet('documents/dataset.txt')
    print(ds.dataset)