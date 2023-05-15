from dataclasses import dataclass


@dataclass
class Item:
    id: int
    title: str
    description: str
    price: int
    photo_link: str


NoteBook = Item(
    id=1,
    title='Ноутбук Lenovo IP Gaming 3',
    description='Выведите игровой процесс киберспортивных дисциплин на новый уровень с помощью устройства, которое поможет опередить конкурентов и занять первые строчки в списках лидеров',
    price=1,
    photo_link="https://items.s1.citilink.ru/1595005_v01_b.jpg"
)
NoteBook2 = Item(
    id=2,
    title='Ноутбук Lenovo IP Gaming 4',
    description='Выведите игровой процесс киберспортивных дисциплин на новый уровень с помощью устройства, которое поможет опередить конкурентов и занять первые строчки в списках лидеров',
    price=100,
    photo_link="https://items.s1.citilink.ru/1595005_v01_b.jpg"
)
items = [NoteBook, NoteBook2]
